# ============================================================
# BLOQUE 1 - AUTENTICACIÓN
# ============================================================

# Diccionario simulado de usuarios
usuarios = {
    "enzo": {
        "pin": 1234,
        "saldo": 250000,
        "bloqueado": False,
        "extraido_hoy": 0
    },
    "dulio": {
        "pin": 4321,
        "saldo": 180000,
        "bloqueado": False,
        "extraido_hoy": 0
    },
    "ramiro": {
        "pin": 1111,
        "saldo": 95000,
        "bloqueado": False,
        "extraido_hoy": 0
    }
}

def formatear_monto(valor):
    """
    Da formato de moneda a un valor numérico, usando punto como
    separador de miles y coma para decimales.
    Si el valor es entero no muestra decimales.
    """
    if valor == int(valor):
        return f"{int(valor):,}".replace(",", ".")
    texto = f"{valor:,.2f}"
    return texto.replace(",", "X").replace(".", ",").replace("X", ".")

def validar_credenciales():
    """
    Solicita usuario y PIN.
    Permite hasta 3 intentos.
    Si supera el límite, la cuenta queda bloqueada.
    """

    usuario = input("Usuario: ").lower().strip()

    if usuario not in usuarios:
        print("\nUsuario inexistente.")
        return None

    if usuarios[usuario]["bloqueado"]:
        print("\nLa cuenta se encuentra bloqueada.")
        return None

    intentos = 3

    while intentos > 0:

        try:
            pin = int(input("PIN: "))

        except ValueError:
            intentos -= 1
            print(f"\nEl PIN debe contener solo números.")
            print(f"Intentos restantes: {intentos}")
            continue

        if pin == usuarios[usuario]["pin"]:
            print("\nAcceso concedido.")
            return usuario

        intentos -= 1

        if intentos > 0:
            print("\nPIN incorrecto.")
            print(f"Intentos restantes: {intentos}")

    usuarios[usuario]["bloqueado"] = True
    print("\nCuenta bloqueada por exceso de intentos.")

    return None

# ============================================================
# BLOQUE 2 - CONSULTA DE SALDO
# ============================================================

def consultar_saldo(usuario):
    """
    Muestra el saldo actual disponible de la cuenta del usuario.
    """
    saldo_actual = usuarios[usuario]["saldo"]
    print(f"\nSu saldo disponible es: ${formatear_monto(saldo_actual)}")

# ============================================================
# BLOQUE 3 - EXTRACCIÓN
# ============================================================

LIMITE_DIARIO = 50000

def realizar_extraccion(usuario):
    """
    Permite retirar dinero de la cuenta.
    Valida saldo suficiente y que no se supere el límite diario acumulado.
    """

    try:
        monto = float(input("\nIngrese el monto a extraer: $"))
        if monto <= 0:
            print("\nError: El monto a extraer debe ser mayor a cero.")
            return

        disponible_diario = LIMITE_DIARIO - usuarios[usuario]["extraido_hoy"]

        if monto > disponible_diario:
            print(f"\nError: El monto supera el límite de extracción diaria.")
            print(f"Límite diario: ${formatear_monto(LIMITE_DIARIO)}")
            print(f"Ya extraído hoy: ${formatear_monto(usuarios[usuario]['extraido_hoy'])}")
            print(f"Disponible para extraer hoy: ${formatear_monto(disponible_diario)}")
            return

        if monto > usuarios[usuario]["saldo"]:
            print("\nError: Saldo insuficiente para realizar la operación.")
            return

        # Resta del acumulador de saldo y suma al acumulador diario extraído
        usuarios[usuario]["saldo"] -= monto
        usuarios[usuario]["extraido_hoy"] += monto
        print(f"\nExtracción realizada. Retire su dinero.")
        print(f"Saldo restante: ${formatear_monto(usuarios[usuario]['saldo'])}")

    except ValueError:
        print("\nError: Debe ingresar un valor numérico válido.")

# ============================================================
# BLOQUE 4 - DEPÓSITOS
# ============================================================

def realizar_deposito(usuario):
    """
    Permite ingresar dinero a la cuenta.
    Valida que el monto sea un número positivo.
    """
    try:
        monto = float(input("\nIngrese el monto a depositar: $"))

        if monto <= 0:
            print("\nError: El monto a depositar debe ser mayor a cero.")
            return

        usuarios[usuario]["saldo"] += monto
        print(f"\nDepósito exitoso. Nuevo saldo: ${formatear_monto(usuarios[usuario]['saldo'])}")

    except ValueError:
        print("\nError: Debe ingresar un valor numérico válido.")

# ============================================================
# BLOQUE 5 - TRANSFERENCIAS
# ============================================================

def realizar_transferencia(usuario):
    """
    Simula una transferencia a otro usuario del sistema mediante validación.
    """
    destino = input("\nIngrese el nombre de usuario del destinatario: ").lower().strip()

    if destino == usuario:
        print("\nError: No puede transferirse dinero a sí mismo.")
        return

    if destino not in usuarios:
        print("\nError: El usuario destinatario no existe.")
        return

    try:
        monto = float(input(f"Ingrese el monto a transferir a {destino.capitalize()}: $"))

        if monto <= 0:
            print("\nError: El monto debe ser mayor a cero.")
            return

        if monto > usuarios[usuario]["saldo"]:
            print("\nError: Saldo insuficiente para transferir.")
            return

        # Operación cruzada de acumuladores
        usuarios[usuario]["saldo"] -= monto
        usuarios[destino]["saldo"] += monto
        
        print("\n¡Transferencia realizada con éxito!")
        print(f"Su saldo actual es: ${formatear_monto(usuarios[usuario]['saldo'])}")

    except ValueError:
        print("\nError: Debe ingresar un valor numérico válido.")

# ============================================================
# BLOQUE 6 - MENÚ PRINCIPAL
# ============================================================

def mostrar_menu():
    print("\n==============================")
    print("      CAJERO AUTOMÁTICO")
    print("==============================")
    print("1 - Consultar saldo")
    print("2 - Extraer dinero")
    print("3 - Depositar dinero")
    print("4 - Transferir dinero")
    print("5 - Cerrar sesión")
    print("==============================")

# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

def main():

    usuario = validar_credenciales()

    if usuario is None:
        return

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consultar_saldo(usuario)

        elif opcion == "2":
            realizar_extraccion(usuario)

        elif opcion == "3":
            realizar_deposito(usuario)

        elif opcion == "4":
            realizar_transferencia(usuario)

        elif opcion == "5":
            print("\nSesión finalizada.")
            break

        else:
            print("\nOpción inválida.")

# ============================================================
# INICIO DEL PROGRAMA
# ============================================================

if __name__ == "__main__":
    main()