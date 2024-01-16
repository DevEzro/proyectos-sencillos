def temperatura():
    celsius = float(input("Introduce los grados en Cº: "))
    faren = int(celsius * 9/5) + 32
    print("\033[1;32m"+"[+]" +'\033[0;m'+f"{celsius} Cº son {faren} Fº")
