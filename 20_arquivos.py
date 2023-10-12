#!/bin/python3

with open ("/home/chimpa/Documents/ArquivoPython.txt" , "w" ) as arquivo:
    arquivo.write(" \n Esta é a melhor maneira de criar um arquivo. \n " )

frase=input("Acrescente uma frase ao arquivo: ")


with open ("/home/chimpa/Documents/ArquivoPython.txt" , "a" ) as arquivo:
    arquivo.write(frase)
