
nome = 'Carlos'
senha = 1234
saldo = 0
tipo_de_conta = ''
programa_ativo = True
iniciando = True

def depositar(valorInformado):
  global saldo
  valor = valorInformado
  saldo += valor
  
def transferencia(valorInformado, numeroDaConta):
  global saldo
  valor = valorInformado
  nConta = numeroDaConta

  if valor > 0 and nConta != 0:
    saldo -= valor
    print(f'Valor foi transferido para conta: {nConta}')
    print(f'Valor: {valor}')
  else:
    print('valor ou o número da conta estão incorretos!')

def saque(valorInformado, senhaInformada):
  global saldo
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
    case 2:
      numeroDaConta = int(input('Informe o numero da conta: '))
      valor = float(input('Valor da transferencia: '))
      transferencia(valor,numeroDaConta)
    case 3:
      valor = float(input("Qual o valor que deseja depositar: "))
      depositar(valor)
    case 4:
      valor = float(input("Qual valor deseja retirar: "))
      senhaAuten = int(input('Informe a senha: '))
      saque(valor, senhaAuten)
    case 5:
      print('Encerrando!')
      global iniciando
      global programa_ativo
      iniciando = False
      programa_ativo = False
    case _:
      print('Desculpe mas não exite essa opção')

def login(nomeDigitado, senhaDigitada):
  if nomeDigitado == nome and senhaDigitada == senha:
    print('\nUsuário confirmado!')
    print('Acessando conta!!!')
    gerenciamento()

  else:
    print(f'O usuário: {nomeDigitado} ou senha: {senhaDigitada} estão incorretas')

# Programa
while iniciando:
  if programa_ativo:
    nomeInformado = str(input("Informe seu nome: "))
    senhaInformada = int(input("Informe a senha: "))
    login(nomeInformado, senhaInformada)
  else:
    break