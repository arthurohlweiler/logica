def selecao_mudou(evento):
    sel = evento.widget.curselection()
    if sel:
        idx =sel[0]
        label.config(
            text=f"{evento.widget.get(idx)} selecinado!")
listbox = tk.Listbox(root)
for item in ["Primeiro", "Segundo", "Terceiro"]:
    listbox.insert(tk.END, item )
listbox.bint("<<listboxselect>>",selecao_mudou)
listbox.pack(expand=True)
label = tk.Label (root, text="Primeiro selecinado!")l
label.pack()