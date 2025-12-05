'''
    Objetivo: Criar um programa que calcula a média e diz se o aluno passou.
'''

# função de calculo
def media(n1,n2,n3):
  soma = n1+n2+n3
  media = soma/2

  return media    

# pedir as 3 notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

print(f"\nSua média é: {media(nota1,nota2,nota3):.2f}")