from datetime import date

programa_ativo = True
precoTotal = 0
carrinho = {
  "Produtos": [],
  "Precos": [],
  "Qt": []
}

while True:
  if programa_ativo:
    prod = str(input("\nProduto: "))
    preco = float(input("Preço: "))
    qtd = int(input("Qtd: "))

    carrinho["Produtos"].append(prod)
    carrinho["Precos"].append(preco)
    carrinho["Qt"].append(qtd)

    print(f'\nProduto: {prod} | Preço: {preco} | Quatidade: {qtd}')
      
    resp = input("\nAdicionar mais itens? ").upper()
    if resp == 'N':
      for produto, preco, quantidade in zip(carrinho["Produtos"], carrinho["Precos"], carrinho["Qt"]):
        print(f"Produto: {produto} | Preço: {preco} | Quantidade: {quantidade}")
        precoTotal += preco*quantidade

      if precoTotal >= 100:
        precoTotal *= 0.90 # 10% desconto
      elif precoTotal > 50:
        precoTotal *= 0.95 # 5% desconto
      else:
        pass

      print(f"\nData: {date.today()} | Total: R$ {precoTotal:.2f}")
      break
    elif resp == "S":
      continue
    else:
      print("opção inválida, encerrando por segurança.")
      break

  else:
    break