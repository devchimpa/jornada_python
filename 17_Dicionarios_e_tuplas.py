#!/bin/python3

#Código explicado trecho a trecho.
usuarios={} #Aqui é criado uma variável vazia, podendo ser dicionario ou conjunto.

emails= ["gmail" , "hotmail" ]#Aqui é criada uma lista de emails, no caso 2 emails.

tupla = list(enumerate(emails)) # Esta tupla está numerando de 0 ao tamanho da lista os emails.

for chave in range(0,len(tupla)): # Para cada variável que vá do 0 a quantidade de emails dentro da tupla, faça:
    print("Email: ", tupla[chave][1]) #Printa o email, a tupla tem dois items, o 1 indica que estamos imprimindo o item que está na segunda posição, a primeira posição é o número.
    usuarios[tupla[chave]]=[input("Digite o nome: ") , input("digite o nível: ")] #Aqui estamos adicionando ao dicionário vazio os valores recebidos pelo input.

for chave, dado in usuarios.items(): # O usuários.items tem duas posições,um onde estão os emails que servem como chaves e outra posição, chamada de dado, que serve como valor.
    print("Usuario: ", chave[0])
    print("Email: ", chave[1])
    print("Nome: ", dado[0])
    print("Nível: " , dado[1])
# Ao printar estamos dizendo qual posição de chave e valor queremos imprimir.
