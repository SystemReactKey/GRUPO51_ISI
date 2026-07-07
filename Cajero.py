# ============================================================
# TRABAJO FINAL INTEGRADOR - ALGORITMOS Y ESTRUCTURAS DE DATOS
# Simulador de Cajero Automático
#
# Integrantes:
# - Dulio Jhoser Cardozo
# - Enzo Mariano Gronda
# - Ramiro Agustín Oru
#
# Comisión: ISI
# Año: 2026
# ============================================================


# ============================================================
# BLOQUE 1 - AUTENTICACIÓN
# Responsable: Enzo Mariano Gronda
# ============================================================

# Diccionario simulado de usuarios
usuarios = {
    "enzo": {
        "pin": 1234,
        "saldo": 250000,
        "bloqueado": False
    },
    "dulio": {
        "pin": 4321,
        "saldo": 180000,
        "bloqueado": False
    },
    "ramiro": {
        "pin": 1111,
        "saldo": 95000,
        "bloqueado": False
    }
}


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
# Responsable: Dulio Jhoser Cardozo
# ============================================================

def consultar_saldo(usuario):
    pass


# ============================================================
# BLOQUE 3 - EXTRACCIÓN
# Responsable: Ramiro Agustín Oru
# ============================================================

def realizar_extraccion(usuario):
    pass


# ============================================================
# BLOQUE 4 - DEPÓSITOS
# ============================================================

def realizar_deposito(usuario):
    pass


# ============================================================
# BLOQUE 5 - TRANSFERENCIAS
# ============================================================

def realizar_transferencia(usuario):
    pass


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