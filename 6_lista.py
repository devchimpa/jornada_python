#!/bin/python3

lista=[]
resposta="s"
while resposta == "s" :
	print("Gostaria de adicionar um item a lista? ")
	entrada=input("Digite S para SIM ou N para NÃO: ")
	resposta=entrada.lower()
	if resposta =="s" :
		lista.append(input("Digite um item: "))
	elif resposta =="n":
		print("programa encerrado.")
	else:
		print("por favor digite uma entrada válida")
print("lista pronta: ")
print(lista)
