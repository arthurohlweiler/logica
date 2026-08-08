import tkinter as tk


root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("800x600")

def classificar_imc (imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Saudável"
    elif imc < 30:
        return "Sobrepeso" 
    else:
        return "Obesidade"

root.mainloop()