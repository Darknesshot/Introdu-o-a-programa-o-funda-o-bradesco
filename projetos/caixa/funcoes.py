from datetime import date

def visualizar(dic):
  precoTotal = 0

  print(f'\n-------------- Data: {date.today().strftime('%d/%m/%Y')} --------------\n')
  for produto, dados in dic.items():
    print(f'Produto: {produto} | Preço: {dados['preco']} | Quantidade: {dados['quantidade']}')
    precoTotal += dados['preco']*dados['quantidade']
    
  if precoTotal >= 100:
    precoTotal *= 0.90 # 10% desconto
  elif precoTotal > 50:
    precoTotal *= 0.95 # 5% desconto
  else:
    pass
  
  print(f'\nTotal: {precoTotal:.2f}')

def pesquisa(item_pesquisado,dic):
  parte = item_pesquisado.lower()
  encontrados = []

  for nome , dados in dic.items():
    if parte in nome.lower():
      encontrados.append((nome,dados))
  
  if encontrados:
    print('\n------ Resultados encontrados ------')
    for nome, dados in encontrados:
      print(f'Produto: {nome} | Preço: {dados['preco']} | Quantidade: {dados['quantidade']}')
  else:
    print(f'Nenhum produto com o nome: {item_pesquisado}, foi encontrado!')

def ediacao(item_editar,dic):
  nomeProduto = item_editar.lower()

  if nomeProduto in dic:
    del dic[nomeProduto]
    print(f'Produto {nomeProduto} excluido com sucesso')
  else:
    print(f'Não exite o produto com o nome {nomeProduto} listado')