def primo():
    numero = int(input("\033[1;37m"+"[*]" +'\033[0;m'+"Introduce un numero entero y positivo: "))
    if numero < 2:
        print("\033[1;33m" + "[!]" +'\033[0;m' +f"EL NUMERO {numero} DEBE SER ENTERO, POSITIVO Y MAYOR QUE 2")
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print("\033[1;31m"+"[X]" +'\033[0;m'+f"El numero {numero} NO es primo.")
            return False
            
    print("\033[1;32m"+"[+]" +'\033[0;m'+f"El numero {numero} SI es primo.")
    return True