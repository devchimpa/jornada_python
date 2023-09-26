#!/bin/bash

nome_completo=input("Insira seu nome completo: ")
nome_dividido= nome_completo.split()

nome= nome_dividido[0]
sobrenome=str(nome_dividido[1:])

print(" Seu sobrenome é: ", sobrenome)
print("Seu nome é: " , nome)
