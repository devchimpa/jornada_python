#!/bin/python3
import base64

print(" **** Gerador de senhas Aleatórias ****")
#frase =input( "Insira a senha para codificar: " )

frase=input("insira o texto: ")
frase_codificada = base64.b64encode(frase.encode("utf-8"))
frase_nova=str(frase_codificada)

letras=(len(frase_codificada))
print("Esta senha codificada fica: ", frase_nova[2:letras])
