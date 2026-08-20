import tkinter as tk

root = tk.Tk()
root.title("Senai - Desenvolvimento de sistemas")
root.config(gb="skyblue")

frame = tk.frame(root, whidth=200, heigth=200)
frame.pack(padx=10, pady=10)

nest_frame = tk.Frame(frame, width=190, height=190, bg="red")
nest_frame.pack(padx=10, pady=10)

root.mainloop()