def buscarPalabra(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            palabra_a_buscar = input("\033[1;37m"+"[*]" +'\033[0;m'+"Ingresa la palabra a buscar: ")
            if palabra_a_buscar in contenido:
                print("\033[1;32m"+"[+]" +'\033[0;m'+f"La palabra '{palabra_a_buscar}' se encuentra en el archivo.")
            else:
                print(f"La palabra '{palabra_a_buscar}' no se encuentra en el archivo.")
    except FileNotFoundError:
        print("\033[1;31m"+"[X]" +'\033[0;m'+"El archivo no se encontró.")
    except Exception as e:
        print(f"Error: {e}")    