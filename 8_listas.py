#!/bin/python3


lista=[]


resposta="s"
while resposta == "s" :
        print("Gostaria de adicionar um item a lista? ")
        entrada=input("Digite S para SIM ou N para NÃO: ")
        resposta=entrada.lower()
        if resposta =="s" :
                inserir_item=input("Digite um item: ").capitalize()
                lista.append(inserir_item)
        elif resposta =="n":
                print("programa encerrado.")
        else:
                print("por favor digite uma entrada válida")
print("lista pronta: ")
lista.sort()
print(lista)

remover_item="s"
while remover_item == "s"  :
        remover_item=input("Gostaria de remover um item? ")
        if remover_item == "s":
                item_selecionado=input("Digite o item a ser removido: ").capitalize()
                lista.remove(item_selecionado)
        elif remover_item == "n":
                break
        else:
                print("Opção inválida.")
print("Lista final: " , lista )
