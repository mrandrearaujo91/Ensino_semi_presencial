"""import random
saladeAula = []

while True:
    aluno = input("Digite o nome do Aluno: ")
    if (aluno =="sair"):
        break
    else:
        saladeAula.append(aluno)
sortudo = random.choice(saladeAula)        
print(f"O Aluno sortudo foi {sortudo}")

import sys
import os 
os.system("cls||clear")
maiornumero=0
menorNumero=sys.maxsize
numeros=[]
for i in range (3):
    numero = int(input(f"Digite o {i+1}º Número: "))
    numeros.append(numero)
    maiorNumero=max(numeros)
    menorNumero=min(numeros)
print(f"O Maior Número é: {maiorNumero}")
print(f"O Menor Número é: {menorNumero}")

soma=0
numeros=[]
while True:
    numero=int (input(f"Digite o Número: "))
    if (numero == 0):
        break
    else:
        numeros.append(numero)
        soma=sum(numeros)
print(soma)        

maiorNumero=0
soma=0
numeros=[]
for i in range(10):
    numero=int(input(f"Digite o {i+1}º Número: "))
    numeros.append(numero)
    maiorNumero=max(numeros)
    soma=sum(numeros)
print(f"Lista: {numeros}")
print(f"O Maior Número é: {maiorNumero}")
print(f"A Soma dos Números é: {soma}")

nomes=[]
for i in range(5):
    nome=input(f"Digite o {i+1}º Nome: ")
    nomes.append(nome)
    nomes.sort()
print(f"Os nomes em Ordem Alfabetica: {nomes}")    

soma=0
numeros = []
for i in range(10):
    valor = int(input(f"Digite o {i+1}º Valor: "))
    numeros.append(valor)
    soma=sum(numeros)
media = soma/10
print(f"Média: {media}")    
"""