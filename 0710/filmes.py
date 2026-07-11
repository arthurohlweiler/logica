def adicionar_filme():
  print("adicinar filme")

def contar_filmes():
  print("contar filmes")

def  info_por_titulo():
  print("info por filme")

def filmes_por_diretor():
  print("filmes por diretor ")

def filmes_por_gênero():
    print("filmes por gênero")

def media_duração():
      print("media duração")



def menu ():
   while True:
    print("\nmenu:")
    print("0- adicionar filmes(opcinal)")
    print("1 - quantidade total de filmes")
    print("2 - informaçoes de um filme pelo titulo") 
    print("3 - filmes de um diretor especifico")
    print("4 - Filmes de um gênero  especifico")
    print("5 - media de duração dos filmes")
    print("6 - sair")

    opc = input (" escolha uma opção:"). strip()

    if opc == "0":
      adicionar_filme()
    elif opc == "1":
      contar_filmes()
    elif opc == "2":
      info_por_titulo()
    elif opc == "3":
      filmes_por_diretor()
    elif opc == "4":
      filmes_por_gênero()
    elif opc == "5":
      media_duração()
    elif opc == "6":
     print ("saindo...")
     break 
    else:
       print("opção inválida . tente novamente.")

if __name__ == "__main__":
   menu()