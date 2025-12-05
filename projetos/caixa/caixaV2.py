from datetime import date
import funcoes as fc

iniciando = True
programa_ativo = True
carrinho = {}

# inicio do programa
while iniciando:
  if programa_ativo:
    prod = str(input("\nProduto: "))
    preco = float(input("Preço: "))
    qtd = int(input("Qtd: "))

    carrinho[prod] = {'preco': preco, 'quantidade': qtd}

    print('\n----------- Produto adicionado -----------')
    print(f'Produto: {prod} | Preço: {preco} | Quatidade: {qtd}')
    print('------------------------------------------\n')
    
    cond = int(input('1-Pesquisar um item\n2-Alterar um item\n3-Finalizar comprar\n4-continuar a compra\n\nqual das opções deseja: '))
    opt = True
    while opt:
      if cond != '':
        if cond == 1:
          nomeProduto = str(input('\nQual o nome do produto: '))
          fc.pesquisa(nomeProduto,carrinho)
          break
        elif cond == 2:
          nomeProduto = str(input('\nDigite o nome do produto: '))
          fc.ediacao(nomeProduto, carrinho)
          break
        elif cond == 3:
          fc.visualizar(carrinho)
          opt = False
          iniciando = False
        elif cond == 4:
          break
        else:
          print('Estamos encerrando por segurança!')
          opt = False
          iniciando = False
      else:
        print('defina um item!!!')
        continue

  else:
    break