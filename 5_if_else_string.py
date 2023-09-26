#!/bin/bash

nome_completo=input("Insira seu nome completo: ")
nome_dividido= nome_completo.split()

nome= nome_dividido[0]
sobrenome=(nome_dividido[1:])

corrige=str(sobrenome)

valor=corrige.replace("[]" , "")


if len(valor) < 1 :
	print("Você não digitou um sobrenome.")
else:
	print(" Seu sobrenome é:" , sobrenome )


print("Seu nome é: " , nome)
