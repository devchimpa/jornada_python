#!/bin/python3


lista=[]

while True:
    print(" Gostaria de adicionar um item a lista?")
    resposta=input(" Pressione S para SIM ou N para Não: ").lower()
    if resposta =="s":
        item=input(" O que gostaria de adicionar? :").capitalize()
        lista.append(item)
        print(lista)
    elif resposta=="n":
        print("Programa finalizado.")
        break
    else: 
        print("Por favor, insira uma opção válida.")

if len(lista) == 0:
    print("Nenhum item foi adicionado. ")
else:
    print("Lista:" , lista )
