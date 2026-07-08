TRABAJO FINAL INTEGRADOR - ALGORITMOS Y ESTRUCTURAS DE DATOS
ESCENARIO: Simulador de Cajero Automático
INTEGRANTES:
 - Dulio Jhoser Cardozo
 - Enzo Mariano Gronda
 - Ramiro Agustín Orue
COMISION: ISI
AÑO: 2026
URL VIDEO: 

DESCRIPCION DEL SISTEMA:
    Simulador de operaciones basicas de un cajero automatico, valida el acceso por nombre de usuario y contraseña, consulta saldo disponible, ademas implementa acciones como extraccion, deposito y transeferencias.
    Como valor añadido, cuenta con control de saldo y limites de extracciones.

REQUISITO:
    Python 3.10 o superior

INSTRUCCIONES DE EJECUCION:
    1) Abrir una terminal (consola / cmd) en la carpeta donde se encuentre el archivo.
    2) Ejecutar el programa utilizando el comando python Cajero.py, en caso de tener como sistema operativo Linux o Mac : python3 Cajero.py
    3) Iniciar secion ingresando con un usuario y pin valido
        USUARIOS DE PRUEBA:
        Usuario    PIN    Saldo inicial
        --------  -----   -------------
         enzo      1234    $250.000
         dulio     4321    $180.000
         ramiro    1111    $95.000

        Se dispone de un maximo de 3 intentos para ingresar el pin correcto.
    4) Elegir la opcion que desea realizar que muestra el menu:
         1 - Consultar saldo
         2 - Extraer dinero
         3 - Depositar dinero
         4 - Transferir dinero
         5 - Cerrar sesión
    5) Límite de extracción diaria: el sistema permite extraer hasta $50.000 por día en total (puede ser en una o varias operaciones dentro de la misma sesión). Si se intenta superar ese límite acumulado, la operación es rechazada y se informa el monto disponible restante.
    6) Para finalizar, seleccionar la opción "5 - Cerrar sesión". Esto también finaliza la ejecución del programa.

IA UTILIZADA: Claude Code
- verificacion correcta de cada funcion del sistema.
- ejecucion de cada caso posible presentado para verificar el uso correcto de manejo de errores.