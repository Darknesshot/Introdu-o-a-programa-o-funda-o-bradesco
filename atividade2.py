'''
Calculadora, requisitos:
1. Pergunta qual operação fazer (+, -, *, /)
2. Pergunta os dois números
3. Faz apenas a operação escolhida
4. Mostra o resultado
'''

# funções para os calculos
def sum(a,b):
  result = a+b
  print(f"O resultado da soma de {a} e {b}: {result}\n")

def sub(a,b):
  result = a-b
  print(f"O resultado da subtração de {a} e {b}: {result}\n")

def div(a,b):
  if a and b != 0:
    result = a/b
    print(f"O resultado da divisão de {a} e {b}: {result}\n")
  else:
    print("mostre um numero valido \n")

def mult(a,b):
  if a and b != 0:
    result = a*b
    print(f"O resultado da divisão de {a} e {b}: {result}\n")
  else:
    print("mostre um numero valido \n")

# execulsão do programa
cond = True
while cond:
  print("Qual calculo vc deseja: \n 1 - soma \n 2 - subtração \n 3 - multiplicação \n 4 - Divivsão \n 5 - Sair")
  calculo = int(input("Fale qual calculo deseja: "))

  match calculo:
    case 1:
      num1 = int(input("Digite o primeiro numero: "))
      num2 = int(input("Digite o segundo numero: "))
      sum(num1,num2)
    case 2:
      num1 = int(input("Digite o primeiro numero: "))
      num2 = int(input("Digite o segundo numero: "))
      sub(num1,num2)
    case 3:
      num1 = int(input("Digite o primeiro numero: "))
      num2 = int(input("Digite o segundo numero: "))
      mult(num1,num2)
    case 4:
      num1 = int(input("Digite o primeiro numero: "))
      num2 = int(input("Digite o segundo numero: "))
      div(num1,num2)
    case 5:
      print("Ok, até a proxima!")
      break