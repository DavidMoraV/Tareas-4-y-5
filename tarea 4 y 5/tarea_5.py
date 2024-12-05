def contador_de_frecuencia(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            texto = archivo.read()
        
        frecuencia = {}
        for letra in texto:
            if letra.isalpha():  # Considerar solo letras
                if letra in frecuencia:
                    frecuencia[letra] += 1
                else:
                    frecuencia[letra] = 1
        return frecuencia

    except Exception as e:
        print(f"Error en el archivo: {e}")
        return None
