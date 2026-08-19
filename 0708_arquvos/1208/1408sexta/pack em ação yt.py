import tkinter as tk 

root = tk.Tk()
root.tiltle("Senai - Desevolvimento de sistemas")
root.geometry("340x100")

tk.Button(root, text="top Button!").pack()
tk.Label(root, Text="Hello Left!").pack(side="left")
tk.Label(root, text= "Hello, Rigth!").pack(saide="right")
tk.checkbutton(root, text="Uma opção na parte inferior!").pack(side=tk.BUTTOM) 

root.mainloop()