from tarea_4 import *
import tarea_4

def main():
    # leer_entero
    entero = tarea_4.leer_entero(prompt="Ingrese un numero entero: ", intentos_max=3, positivos=True)
    print(f"Numero entero ingresado: {entero}") # permitimos solo 3 intentos

    # leer_flotante
    flotante = tarea_4.leer_flotante(prompt="Ingrese un número decimal: ", intentos_max=3, positivos=True)
    print(f"Numero con decimales ingresado: {flotante}")

    # obtener_archivo
    archivo = tarea_4.obtener_archivo("prueba.txt", finalizar_programa=False)
    if archivo:
        contenido = archivo.read()
        archivo.close()
        print(f"Contenido del archivo:\n{contenido}")

    # Probando mostrar_menu
    opciones = ["Opción 1", "Opción 2", "Opción 3"]
    tarea_4.mostrar_menu(titulo_menu="Mi Menú Personalizado", lista_opciones=opciones, opciones_caracter="alfanumérico")

# menu muestra el titulo al inicio - opciones es lo que se mostrara( [] y lista)
# caracter como enumeran las opciones del menu

if __name__ == "__main__":
    main()
