# Programa de converção de temperatura

# converter de celsius para fahrenheit
def celsiusInFahrenheit(celsius):
  fahrenheit = (celsius - 32) * 5/9
  print(f"A temperatura de Celsius é: {celsius}°C, convertida em Fahrenheit é: {round(fahrenheit, 2)}°F\n")

# Converter de fahrenheit para celsius
def fahrenheitInCelsius(fahrenheit):
  celsius = (fahrenheit * 9/5) +32
  print(f"A temperatura de Fahrenheit é: {fahrenheit}°F, convertida em Celsius é: {celsius}°C\n")

# converter de celsius em Kelvin
def celsiusInKelvin(celsius):
  kelvin = celsius +273.15
  print(f"A temperatura de celsius é: {celsius}°C, convertida em Kelvin é: {kelvin}°K\n")


cond = True
while cond:
  print("Qual conversão você deseja:\n 1 - De celsius p/ Fahrenheit\n 2 - De Fahrenheit p/ celsius\n 3 - De celsius p/ kelvin\n 4 - Sair\n")

  conversao = int(input("Degite qual conversão deseja: "))
  match conversao:
    case 1:
      valor = int(input("Digite o valor celsius em número inteiro: "))
      celsiusInFahrenheit(valor)
    case 2:
      valor = int(input("Digite o valor de fahrenheit em numero inteiro: "))
      fahrenheitInCelsius(valor)
    case 3:
      valor = int(input("Digite o valor de celsius em número inteiro: "))
      celsiusInKelvin(valor)
    case 4:
      print("ok, até a proxima")
      break
