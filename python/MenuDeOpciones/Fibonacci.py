def calcula_fibonacci():
    
    try:
        print("\033[1;37m"+"[*]" +'\033[0;m'+"Ingresa la cantidad de numeros que quieres mostrar de la secuencia")
        numFibo = int(input("\033[1;33m" + "[!]" +'\033[0;m' "DEBE SER ENTERO Y POSITIVO: "))
        if numFibo < 0:
            print("\033[1;31m"+"[X]" +'\033[0;m'+"El número {numFibo} no es entero o positivo.")
            return
        
        fibonacci = [0, 1]
        while len(fibonacci) < numFibo:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        print("\033[1;32m"+"[+]" +'\033[0;m'+f"Primeros {numFibo} numeros de la sucesión de Fibonacci: {fibonacci}")
    
    except ValueError:
        print("\033[1;33m" + "[!] Por favor, introduce un número entero válido.")
