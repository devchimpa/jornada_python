#!/usr/bin/python3
# Devchimpa - 14/09/2024

print("Este código separa as letras do seu nome com um dígito separador.")
while True :
    entrada=input("Digite seu nome: ")
    if entrada.isdigit():
        print("Digite um nome...")
    else:
        nome=entrada.capitalize()
        print(f"Olá, {nome}.")
        separador=input("Digite um separador: ")
        indice= 0
        novo_nome = ''
        while indice < len(nome):
            letra=(nome[indice]) 
            novo_nome += (f'{letra}{separador}')
            indice += 1
    break

print(novo_nome)
