#!/bin/python3

#dicionarios em python

conjunto={"Pinheiro", "Auracária" , "Sequóia" }

print("Um conjunto também é feito com chaves")
print(type(conjunto))

print(conjunto)

deletar=input("Digite um item para ser removido: ").capitalize()

print(deletar)

conjunto.remove(deletar)

print(conjunto)

adicionar=input("Digite um item para adicionar: ").capitalize()

conjunto.add(adicionar)

print(conjunto)
