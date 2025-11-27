from datetime import date

programa_ativo = True
precoTotal = 0
carrinho = {
  "Produtos": [],
  "Precos": []
}

while True:
  if programa_ativo:
    prod = str(input("\nProduto: "))
    preco = float(input("Preço: "))
    qtd = int(input("Qtd: "))

    carrinho["Produtos"].append(prod)
    total = preco*qtd
    carrinho["Precos"].append(total)
      
    resp = input("\nAdicionar mais itens? ").upper()
    if resp == 'N':
      for produto, preco in zip(carrinho["Produtos"], carrinho["Precos"]):
        print(f"Produto: {produto} | Preço: {preco}")
        precoTotal += preco

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