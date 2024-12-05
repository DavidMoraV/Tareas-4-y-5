def leer_entero(prompt="introduzca el numero: ", intentos_max=None, positivos=False):
    intentos = 0      #intentos max es la cantidad permitida
    while intentos_max is None or intentos < intentos_max:
        try:
            valor = int(input(prompt))
            if positivos and valor < 0:
                print("El numero no puede ser negativo.")
                intentos += 1
                continue     # Si la entrada no es un numero entero notifica al usuario y solicita nuevamente
            return valor
        except ValueError:
            print("introduzca un numero entero válido.")
            intentos += 1
    if intentos_max and intentos >= intentos_max:
        raise Exception("Cantidad maxima de intentos alcanzada.")

# Indica si solo se deben aceptar numeros positivos (por defecto es False)
def leer_flotante(prompt="introduzca el numero: ", intentos_max=None, positivos=False):
    intentos = 0
    while intentos_max is None or intentos < intentos_max:
        try:
            valor = float(input(prompt))
            if positivos and valor < 0:
                print("El numero no puede ser negativo.")
                intentos += 1
                continue
            return valor
        except ValueError:
            print("introduzca un numero con decimales valido.")
            intentos += 1

    if intentos_max and intentos >= intentos_max:
        raise Exception("Cantidad maxima de intentos alcanzada.")
    
# Si el archivo no existe, escribe el error en un archivo  nuevo llamado error.log
def obtener_archivo(ruta_archivo, finalizar_programa=True):
    try:
        return open(ruta_archivo, 'r')
    except FileNotFoundError:
        with open('error.log', 'a') as error_log:  #esto abre el archivo adicional.
            error_log.write(f"Archivo no encontrado: {ruta_archivo}\n")
        print("Archivo no existe.")
        if finalizar_programa:
            exit(1)
        else:
            return input("Introduzca la ruta correcta: ")

def mostrar_menu(titulo_menu="MENU", lista_opciones=[], opciones_caracter="numerado"):

    print(titulo_menu)
    if opciones_caracter == "numerado":
        for i, opcion in enumerate(lista_opciones, 1):
            print(f"{i}. {opcion}")
    else:
        for i, opcion in enumerate(lista_opciones):
            print(f"{chr(65 + i)}. {opcion}")

# menu muestra el titulo al inicio - opciones es lo que se mostrara( [] y lista)
# caracter como enumeran las opciones del menu
