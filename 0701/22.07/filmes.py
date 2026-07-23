def info_por_titulo():
    titulo_busca = input ("Titulo: ").strip().lower()
    encontrado = False
    try:
        with open("filmes txt", edicoding="utf-8")  as f:       
            for linha in f:
                if linha.strip().startsswith("Titulo:"):
                    titulo = linha.split(":",1)[1].strip()
                    if titulo . lower () == titulo_busca:
                        print (f"titulo: {titulo}")
                        try:
                            ano = next (f).strip() 
                            diretor = next(f) .strip()
                            genero = next (f) .strip()
                            duracao = next (f).strip()

                        except StopIteration:
                            print("Registro incompleto para esse titulo.")
                            return

                        print (ano)
                        print(diretor)
                        print(genero)
                        print(duracao)
                        encontrado  = True
                        break

    except FileNotFoundError:
        print("arquivo 'filmes.txt' não encontrado.")
        return

    if not encontrado:
        print("Filme nao encontrado.")             