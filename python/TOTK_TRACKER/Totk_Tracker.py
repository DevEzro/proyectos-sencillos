import os #Update
import tkinter as tk

def kologs(label):
    kologs = int(label.cget("text"))
    suma_kologs = kologs+1
    label.config(text=str(suma_kologs))

def santuarios(label):
    santuarios = int(label.cget("text"))
    suma_santuarios = santuarios+1
    label.config(text=str(suma_santuarios))

def raices(label):
    raices = int(label.cget("text"))
    suma_raices = raices+1
    label.config(text=str(suma_raices))
#--------------------------------

ventana = tk.Tk()
ventana.title("TOTK Tracker")

# Obtener la ruta del directorio actual del script
ruta_script = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta del icono relativa al directorio del script
ruta_icono = os.path.join(directorio_script, "Iconos", "totk32.ico")
#Cambiar ruta
#ventana.iconbitmap('C:\\Users\\Usuario\\Desktop\\TOTK_TRACKER\\Iconos\\totk32.ico')
ventana.iconbitmap(ruta_icono)
#--------------------------------

ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)
ventana.rowconfigure(2, weight=1)
#--------------------------------

valor_label_kolog = tk.Label(ventana, text = "0")
valor_label_kolog.grid(row=0, column=0)
btn_suma_kolog = tk.Button(ventana, text="+ 1 Kolog", command=lambda: kologs(valor_label_kolog))
btn_suma_kolog.grid(row=0, column=1)

valor_label_santuarios = tk.Label(ventana, text = "0")
valor_label_santuarios.grid(row=1, column=0)
btn_suma_santuarios = tk.Button(ventana, text="+ 1 Santuario", command=lambda: santuarios(valor_label_santuarios))
btn_suma_santuarios.grid(row=1, column=1)

valor_label_raices = tk.Label(ventana, text = "0")
valor_label_raices.grid(row=2, column=0)
btn_suma_raices = tk.Button(ventana, text="+ 1 Raiz", command=lambda: raices(valor_label_raices))
btn_suma_raices.grid(row=2, column=1)
#--------------------------------

btn_suma_kolog.grid()
btn_suma_santuarios.grid()
btn_suma_raices.grid()

ventana.mainloop()
#--------------------------------


''' SIN INTERFAZ
kologs = 72
santuarios = 62
raices = 57
opcion = " "

while (opcion != "0"):
    print("\033[1;32m"+"[K]" +'\033[0;m'+f"KOLOGS: {kologs}")
    print("\033[1;36m"+"[S]" +'\033[0;m'+f"SANTUARIOS: {santuarios}")
    print("\033[1;31m"+"[R]" +'\033[0;m'+f"RAICES: {raices}")
    opcion = input("S -> SANTUARIOS, K -> KOLOGS, R -> RAICES: ")
    if (opcion == "S" ):
        santuarios+=1
    elif (opcion == "K"):
        kologs+=1
    elif (opcion == "R"):
        raices+=1
    elif (opcion == "0"):
        break
'''
