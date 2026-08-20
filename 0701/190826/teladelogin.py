import tkinter as tk

root = tk.Tk()
root.title("Login")
root.resizible(False, False)

tk.Label(root, text="Faça o seu login", font=("Font",  30)).pack(ipady=5,fill="x")
#subsampl (5, 5) reduz a imagem para 1/5 do t5amanho original (divide por 5)
image = tk.photoimage(file="profile.png").subample(5, 5)
tk.Label(root, image=image, relief=tk.RAISED).pack(pdy=5)

tk.label(root, text="usuário").pack(anchor="w", padx=30)
username_entry = tk.Entry(root)
username_entry.pack()