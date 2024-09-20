import BuscarPalabra
import Fibonacci
import Primo
import Temperatura

class Main:
    #FUNCIONES
    def menu(): #MENU
        print("\n")
        print("ELIJE UNA OPCION")
        print("******************************")
        print("*                            *")
        print("*      1-BUSCAR PALABRA      *")
        print("*   2-CALCULAR FIBBONACCI    *")
        print("*     3-VERIFICAR PRIMO      *")
        print("*  4-CONVERTIR TEMPERATURA   *")
        print("*           0-SALIR          *")
        print("*                            *")
        print("******************************")

    def salir(): #0-SALIR
        """Sale del programa"""
        exit()

    #MÉTODO PARA COMPROBAR LA RUTA DE 1-BUSCAR PALABRA
    def comprueba():
        try:
            ruta_archivo = input("Ingresa la ruta del archivo: ")
            entrada = int(input("Ingresa 1 para buscar palabra: "))

            if entrada == 1:
                BuscarPalabra.buscarPalabra(ruta_archivo)
            elif entrada == 2:
                # Otras operaciones si entrada es 2
                pass
            else:
                print("Entrada no válida")
        except ValueError:
            print("Ingresa un número válido.")
        except Exception as e:
            print(f"Error: {e}")
            BuscarPalabra.buscarPalabra(ruta_archivo)

#ESTRUCTURA DE EJECUCCION
    
    while True:
        try:
            menu()
            entrada = int(input("\033[1;37m"+"[*]" +'\033[0;m'+"Introduce una opcion de las mostradas (0-4): "))
            print("\033[1;36m"+"[->]" +'\033[0;m'+"Se ha seleccionado la opcion ", entrada,":")

            if entrada == 0:
                print("\033[1;31m"+"[-]" +'\033[0;m'+ "Terminando el programa]") 
                break
            elif entrada == 1:
                comprueba()
                pass
            elif entrada == 2:
                Fibonacci.calcula_fibonacci()
                pass
            elif entrada == 3:
                Primo.primo()
                pass
            elif entrada == 4:
                Temperatura.temperatura()
                pass
            else:
                print("Opción no válida. Introduce un numero entre el 0 y 4 inclusive.")
        except ValueError:
            print("Ingresa un número válido.")
        except Exception as e:
            print(f"Error: {e}")

    
    
    
    
