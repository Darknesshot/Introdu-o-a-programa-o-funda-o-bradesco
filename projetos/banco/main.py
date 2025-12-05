
nome = 'Carlos'
senha = 1234
saldo = 0
tipo_de_conta = ''
programa_ativo = True
iniciando = True

def depositar(valorInformado):
  valor = valorInformado
  

def saque(valorInformado, senhaInformada):
  valor = valorInformado
  senhaAutentificacao = senhaInformada
  if saldo <= 0 and senhaAutentificacao == senha:
    print("Não exite saldo em conta!")
  else:
    saldo -= valor
    print(f"Valor debitado {valor}\nSaldo em conta: {saldo}")

def gerenciamento():
  print('O que deseja:\n1 - Dados da conta\n2 - Transferencia\n3 - Depositar\n4 - Saque\n5 - Sair')
  opcao = int(input('\n'))
  match opcao:
    case 1:
      print("------------ Dados da conta ------------\n")
      print(f"Nome do usuário: {nome}\nSaldo em conta: {saldo}")
    case 3:
      valor = float(input("Qual o valor que deseja depositar: "))
    case 4:
      valor = float(input("Qual valor deseja retirar: "))
      senhaAuten = int(input('Informe a senha: '))
      saque(valor, senhaAuten)
    case _:
      print('Desculpe mas não exite essa opção')

def login(nomeDigitado, senhaDigitada):
  if nomeDigitado == nome and senhaDigitada == senha:
    print('\nUsuário confirmado!')
    print('Acessando conta!!!')

  else:
    print(f'O usuário: {nomeDigitado} ou senha: {senhaDigitada} estão incorretas')

while iniciando:
  if programa_ativo:
    nomeInformado = str(input("Informe seu nome: "))
    senhaInformada = int(input("Informe a senha: "))
    login(nomeInformado, senhaInformada)
  else:
    break