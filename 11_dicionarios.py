#!/bin/python3

#dicionarios em python

zoologico={}

chave=input("Insira a chave: ")
item=input("Insita o item 1: ")
item_dois=input("insira o item 2: ")

zoologico[chave] = [item , item_dois]
print("\n")
print("Esta é o dicionario completo.")
print(zoologico)
print("estas são as chaves")
print(zoologico.keys())
print("estes sao os valores")
print(zoologico.values())
