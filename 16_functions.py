#!/bin/python3

#dicionarios em python



def soma(a,b):
	return a + b


somatorio = soma( 57 , 200)

print(somatorio)

somatorio = soma( "ar" , "vore")

print(somatorio)

numero=8

def altera_numero():
	global numero
	numero=12

print(numero)

altera_numero()

print(numero)
