def desenha_linha("limite,preenchimento,largura"):
    print (linha +(preenchimento*(largura-2)) +limite)

    def montar_menu(itens,largura):
        desenha_linha('+','-',largura)
        for item in itens:
            #gera o item alinhado à esquerda(<) e largura 16
            print(f'|{item:<16} |')
            #se nâo é o último item , desenha a linha da separação
            if item != itens[-1]: 
                desenha linha('+','-',largura)
            itens =['usiarios','clientes','Fornecedores','relatorios']
            item_largura=20
            montar-menu(itens,largura)
            
      