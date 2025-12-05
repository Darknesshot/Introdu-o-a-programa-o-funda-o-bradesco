from datetime import date

iniciando = True
programa_ativo = True
precoTotal = 0
carrinho = {}

# finalização do código e abilitação da regra de negócio
def visualizar(dic):
  global precoTotal
  for produto, dados in dic.items():
    print(f'Produto: {produto} | Preço: {dados['Preco']} | Quantidade: {dados['Quantidade']}')
    precoTotal += dados['Preco']*dados['Quantidade']
  
  # regra de negócio
  if precoTotal >= 100:
    precoTotal *= 0.90 # 10% desconto
  elif precoTotal > 50:
    precoTotal *= 0.95 # 5% desconto
  else:
    pass

# mecanismo de pequisa
def pesquisa(item_pesquisado,dic):
  parte = item_pesquisado.lower()
  encontrados = []

  for nome , dados in dic.items():
    if parte in nome.lower():
      encontrados.append((nome,dados))
  
  if encontrados:
    print('\n------ Resultados encontrados ------')
    for nome, dados in encontrados:
      print(f'Produto: {nome} | Preço: {dados['Preco']} | Quantidade: {dados['Quantidade']}')
  else:
    print(f'Nenhum produto com o nome: {item_pesquisado}, foi encontrado!')

# mecanismo para manipulação/alterações do dicionário
def ediacao(item_editar,dic):
  pass

# inicio do programa
while iniciando:
  if programa_ativo:
    prod = str(input("\nProduto: "))
    preco = float(input("Preço: "))
    qtd = int(input("Qtd: "))

    carrinho[prod] = {'Preco': preco, 'Quantidade': qtd}

    print('\n----------- Produto adicionado -----------')
    print(f'Produto: {prod} | Preço: {preco} | Quatidade: {qtd}')
    print('------------------------------------------\n')
    
    cond = int(input('1-Pesquisar um item\n2-Alterar um item\n3-Finalizar comprar\n4-continuar a compra\nqual das opções deseja: '))
    opt = True
    while opt:
      if cond != '':
        if cond == 1:
          nomeProduto = str(input('\nQual o nome do produto: '))
          pesquisa(nomeProduto,carrinho)
          break
        elif cond == 2:
         pass
        elif cond == 3:
          print(f'\n-------------- Data: {date.today().strftime('%d/%m/%Y')} --------------\n')
          visualizar(carrinho)
          print(f'\nTotal: {precoTotal:.2f}')
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