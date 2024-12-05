
from tarea_5 import contador_de_frecuencia

nombre_archivo = 'texto.txt'
resultado = contador_de_frecuencia(nombre_archivo)

if resultado is not None:
    for letra, cantidad in resultado.items():
        print(f"{letra}: {cantidad}")
else:
    print("No se pudo leer el archivo.")
