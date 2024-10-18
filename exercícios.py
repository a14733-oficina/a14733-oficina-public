print("hello world")
valorA = float(input("insira um valor entre 1-20: "))
valorB = float(input("insira um valor entre 1-20: "))
soma = (valorA + valorB)
media = (soma/2)
print (media)

if (float (media) < 10.0):
  print("negativa")
if (float (media) >= 10.0):
  print("positiva")
  #EX0.1
  """
  Declara uma variável chamada "idade" e atribuiu a tua idade.
  Declara uma variável chamada "nome" e atribuiu o teu nome.
  Imprima no ecrã a frase "O meu nome é [nome] e tenho [idade] anos."
  """
  idade = input("Insira a sua idade: ");
  nome = input("Insira o seu nome: ")
  print(f"O meu nome é {nome} e tenho {idade} an   
#EX0.2
"""
Escreve um programa que imprima "Olá, mundo!" no ecrã.
Cria uma variável chamada "fruta" e atribuiu o nome de uma fruta.
Imprime no ecrã a frase "Eu gosto de [fruta]."
"""
print("Olá Mundo!")
fruta = "morango";
print(f"Eu gosto de {fruta}.")
#EX0.3
"""
Solicita ao utilizador para digitar o nome.
Imprime no ecrã uma saudação personalizada utilizando o nome fornecido.
Pede ao utilizador para digitar um número inteiro.
Imprime o dobro desse número.
"""
nome =input("Insira um nome: ")
print(f"Olá my g {nome}: ")
n =int(input("Insira um numero: "))
dobro = n * 2
print(f"o dobro de {n} é {dobro}")
#EX1.1
""""
Elabora um programa que imprima a mensagem “Bem-vindos ao Python!”, precedida por uma linha em branco
"""

print("\nBem-vindos ao Pyton")
#EX1.2
""""""Elabora um programa que imprima a mensagem “José, bem-vindo ao Python!”, precedida por uma linha em branc"""
print("\nJosé, bem-vindo ao Python!,")
#EX1.3
"""
Elabora um programa que atribua a mensagem a uma variável e, em seguida, imprima o valor da variável
"""
mensagem=(
"""
 _   _      _ _        __        __         _     _ _ 
| | | | ___| | | ___   \ \      / /__  _ __| | __| | |
| |_| |/ _ \ | |/ _ \   \ \ /\ / / _ \| '__| |/ _` | |
|  _  |  __/ | | (_) |   \ V  V / (_) | |  | | (_| |_|
|_| |_|\___|_|_|\___/     \_/\_/ \___/|_|  |_|\__,_(_)
""")
print(mensagem)
#Ex1.4
"""

Elabora um programa que atribua o nome, a idade e a localidade de residência do aluno a três variáveis e imprima os valores dessas variáveis

"""
nome= "tiago"
idade= int("15")
localidade= "trofa"
print(f"{nome},tem {idade} anos e reside na {localidade}")
#EX1.5
"""Elabora um programa que intercale a designação da linguagem de programação e o nome do aluno na mensagem"""
lingprog="pyton"
nome="tiago"
print(f"O {nome} sabe programar em {lingprog}")
#EX1.6
"""
Elabora um programa que alinhe à direita, à esquerda e ao centro a mensagem “Bem-vindo ao Python!” num campo de edição com 50 carateres.
"""

print(f"{'Bem-vindo ao Python!' : <50} ")
print(f"{'Bem-vindo ao Python!' : ^50} ")
print(f"{'Bem-vindo ao Python!' : >50} ")
#EX1.7
"""
Elabora um programa que desenvolva o algoritmo de um programa que permita calcular o perímetro e área de uma circunferência a partir do valor do raio.
"""
raio = float(input("insira o raio:  "))
perimetro= 2 * 3,14 * raio
print ("O perimetro é",raio)
#EX1.8
"""Elabora um programa que imprima a data e horas correntes nos seguintes formatos:
02-10-2024
02-10-2024 16:11:20
10-02-2024 16:11:20
02/10/24
16:11:20
"""
import datetime
x = datetime.datetime.now()

dia = x.strftime("%d")
mes= x.strftime("%m")
ano= x.strftime("%y")
hora= x.strftime("%X")
print(f"{dia}-{mes}-{ano}  {hora}")
#EX1.8
"""Elabora um programa que imprima a data e horas correntes nos seguintes formatos:
02-10-2024
02-10-2024 16:11:20
10-02-2024 16:11:20
02/10/24
16:11:20
"""
import datetime
x = datetime.datetime.now()



dia = x.strftime("%d")
mes= x.strftime("%m")
ano= x.strftime("%y")
hora= x.strftime("%X")
print(f"{dia}-{mes}-{ano} ")
print(f"{dia}-{mes}-{ano}  {hora}")
print(f"{mes}-{dia}-{ano}  {hora}")
print(f"{mes}/{dia}/{ano} ")
print(f"{mes}:{dia}:{ano} ")
#EX1.9
"""
Elabora um programa que leia o número mecanográfico de um atleta, assim como a sua pontuação. O número é inteiro e a pontuação final é real.
Digite o número do atleta: 12304
Digite a pontuação final: 7.89
O atleta número 12304 obteve 7.89 pontos.
"""
nome= input("Insira o número do atleta: ")
pontos= input("Insira  a pontação do atleta: ")
print(f"O atleta {nome} e a pontuação foi de {pontos} pontos")
nota = float(input("Insira a nota: "))

if nota > 10:
    print("nota é maior que 10")
elif nota == 10:
    print("nota é igual a 10")
else:
    print("nota é menor que 10")
A28
  print("Hello world")
  """
  escreve um progranma que faça o computador pensar em1 numero inteiro entre 0 e 5 e peça para o usuario descobrir qual foi o numero escolhido pelo computador e dizer se o usuario perdeu ou ganhou
  """
  import random 
  n = random.randint(0,5)
  #print(f"O numero secreto é {n}")
  palpite = int(input("Insira um numero de 0 a 5: "))    
  if palpite > n:
      print("O numero inserido é maior do que o meu!")
  elif palpite < n:
       print("O teu numero é menor do que o meu")
  else:
    print("Acertas-te o meu numero")
A29
"""
se ele utrapassar 80km mostre 1 mensagem a dizer q foi multado a multa vai custar 7 euros
""" 
print("hello world")
v = int(input("Insira a velocidade do carro: "))
multa = ( v )-80
valor= (Multa)*7
if v > 80 :
print(f"Foste multado excedeste o limite de velocidade em {multa} km/h e vais pagar  {valor} ")
else: 
print("estas a velocidade certa")

f1
"""
Exercício FP1: Verificar se um número é positivo, negativo ou zero.
Escreve um programa em Python que peça ao utilizador para introduzir um número e verifica se ele é positivo, negativo ou igual a zero.
Dica: Usa as estruturas condicionais if, elif e else.

"""
print("Hello world")
n = int(input("Insirir o numero: "))
if n> 0 :
  print("positivo")
elif n< 0: 
  print("negativo")
else: 
   print("igual a 0")
    f2
"""
Exercício FP2: Verificar se um número é par ou ímpar.
Escreve um programa que peça ao utilizador um número inteiro e verifica se ele é par ou ímpar.
Dica: Para verificar se um número é par, utilize a operação de módulo %.

"""



n =int(input("Insira 1 numero: "))
if n % 2 == 0 :
  print("par")
else:
  print("impar")
f3
"""
Exercício FP3: Calcular a nota final de um aluno.
Elabora um programa que pergunte ao utilizador a nota final de um aluno e verifica a classificação de acordo com a seguinte tabela:
Nota inferior a 10: "Reprovado"
Nota entre 10 e 14: "Suficiente"
Nota entre 15 e 17: "Bom"
Nota superior a 17: "Muito Bom"


"""
nota= int(input("Insira a sua nota: "))
if nota <10 :
  print("reprovado")
elif nota >=10 and nota <=14:
  print("suficiente")
elif nota >=15 and nota <=17:
  print("bom")
elif nota >17:
  print("muito bem")
f4
"""
Exercício FP4: Conversor de temperaturas.
Cria um programa que pergunte ao utilizador uma temperatura em graus Celsius e a converta para Fahrenheit, Kelvin ou ambas. O utilizador deve escolher a unidade de destino (Fahrenheit ou Kelvin), e o programa deve exibir o valor convertido.

Fórmulas:

Fahrenheit = Celsius * 9/5 + 32
Kelvin = Celsius + 273.15

"""
temp = float(input("Insira a temperatura em Celsius: "))
u = str(input("Insira a unidade de destino Fahrenheit(F) ou Kelvin(K) ou ambas(A): "))
if u == "F":
  F = temp * 9/5 +32
  print(f"A temperatura em fahrenheit é {F} ")
elif u == "K":
  K = temp + 273.15
  print(f"A temperatura em kelvin é {K} ")
elif u == "A":
  print(f"A temperatura em Fahrenheit é {F}  e em Kelvin é {K}.")
else:
  print("Valor invalido.")

        f5
"""
Exercício FP5: Cálculo de impostos
Crie um programa que peça ao utilizador o seu salário mensal e calcule o imposto de acordo com a seguinte tabela:
""""
        
salario = int(input("Insira o seu salario: "))
inposto1 = salario * 0.10
inposto2 = salario * 0.20
percentagem1 = salario - inposto1
percentagem2 = salario - inposto2
if salario<= 1000:
  print("estas sem inpostos")
elif salario> 1001 and salario <= 2000:
  print(f"Salario apos imposto de 10 % é {percentagem1: .2f}$ ")
else:
  print(f"Salario apos imposto de 20% é {percentagem2: .2f}$ ")

"""
Exercício FP6: Imprimir números de 1 a 10.
Escreve um programa em Python que use um ciclo for para imprimir todos os números de 1 a 10.
"""
i = 1
while i < 11:
  print(i)
  i += 1
"""Exercício FP8: Contagem de vogais numa string.
Escreve um programa que peça ao utilizador para introduzir uma frase e utilize um ciclo for para contar quantas vogais (a, e, i, o, u) existem na frase."""
frase = input("Insira uma frase: ")
vogais = 0
for letra in frase:
  if letra in "aeiouAEIOU":
    vogais += 1
print("A frase tem", vogais, "vogais"
          """Exercício FP9: Listar múltiplos de 5.
          Escreve um programa que utilize um ciclo for para listar todos os múltiplos de 5 entre 1 e 50.
          """
          for i in range(1, 51):
            if i % 5 == 0:
              print(i)
i = 1 
soma = 0
while i <= 1000:
  soma += i 
  i += 1
  print(soma)
"""
Exercício FP6: Imprimir números de 1 a 10.
Escreve um programa em Python que use um ciclo for para imprimir todos os números de 1 a 10.
"""
for x in range(1,11):
  print(x)
"""Exercício FP8: Contagem de vogais numa string.
Escreve um programa que peça ao utilizador para introduzir uma frase e utilize um ciclo for para contar quantas vogais (a, e, i, o, u) existem na frase."""
frase= str(input ("Insira uma frase: "))
vogais = 0
for letra in frase:
  if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    vogais += 1
print(f"A frase tem {vogais} vogais.")
"""Exercício FP9: Listar múltiplos de 5.
Escreve um programa que utilize um ciclo for para listar todos os múltiplos de 5 entre 1 e 50.
"""
temporario = 0
for i in range (1,51):
  if temporario < 50:
      temporario = i * 5
      print(temporario)
"""Exercício FP10: Verificar se um número é primo.
Escreve um programa que crie uma lista de 5 números inteiros, pede ao utilizador para introduzir cada número e, em seguida, calcula e exibe a média desses números.
"""
notas =[]
for i in range (0,5):
     p=int(input("Escreve um numero inteiro: "))
     notas.append(p)#adiciona um elemento a lista
soma = sum(notas)# cacula o n total de elementos da lista
x= len(notas)#devolve o n total de elementos  a lista
media = (soma / x )
print(media)
"""Exercício FP11: Verificar se um número é primo.
Escreve um programa que peça ao utilizador um número inteiro e verifique se ele é primo. Um número primo é divisível apenas por 1 e por ele mesmo. O programa deve utilizar um ciclo for para testar se o número é divisível por algum outro número.
"""
n = int(input("Numero: "))
divisores= 0
if n >=1:
     for i in range(1,n):
          if n % i !=0: #verifica se o resultado da divisão é zero
               divisores = divisores +1 #incrementa o contador de divisores
          elif divisores ==2: 
               print(n,"é primo")
          else:
               print(n,"nao é primo")
               break
elif n ==0:
     print(n,"é zero")
else:
     print(n,"é negativo")
"""Exercício FP12: Gerar uma lista de números pares.
Cria um programa que utilize a função range() e um ciclo for para gerar uma lista com todos os números pares entre 1 e 20 e imprima a lista.
"""
x = 0
for i in range(1,21):
     if x <20:
          x = i * 2
          print(x)

"""Exercício FP13: Inverter uma string.
Escreve um programa que peça ao utilizador para introduzir uma palavra ou frase e utilize um ciclo para imprimir a string invertida.
"""
texto =str(input("Insira uma frase: "))#pedir ao texto ao user
textoinv = texto [::-1]#script para inverter o texto
print (textoinv) #printar o texto invertido https://www.w3schools.com/python/numpy/numpy_array_slicing.asp
"""Exercício FP14: Tabuada de multiplicação
Escreve um programa que gere a tabuada de multiplicação de um número introduzido pelo utilizador. O programa deve utilizar um ciclo for para calcular e exibir a tabuada até 10.
"""
num = int(input("Insira o número: "))
for i in range(1,11):
  mult= num * i
  print(f"{num} x {i} = {mult}")#printf porque tem variaveis
  num = int(input("Insira o número: "))
  i = 1
  while i < 11:
    mult= num * i
    print(f"{num} x {i} = {mult}")#printf porque tem variaveis
    i += 1


  
