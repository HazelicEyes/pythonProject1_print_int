lista = [1, 3, 5, 7]; print(type(lista))
lista_animal = ["cachorro", "gato", "elefante"]

tupla = (1, 10, 20, 22, 345); print(type(tupla))
print(len(tupla))
print(len(lista_animal))

tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)
















# print(lista_animal[1])
# nova_lista = lista * 3
# print(nova_lista)

# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
#
# lista.reverse()
# lista_animal.reverse()
#
# x = input("Digite um animal: ")


# if x in lista_animal:
#     print("ha", x, "na lista animal")
# else:
#     print("não ha", x, "na lista animal")
#     lista_animal.append(x)
#     print(lista_animal)
#
# lista_animal.remove(x)
# print(lista_animal)

# lista_animal.pop()
# print(lista_animal)

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)            #ou print(sum(lista)) print(max(lista))


# if x in lista_animal:
#     print("ha", x, "na lista animal")
#     while x in lista_animal:
#         x = input("Digite um animal: ")
#
# else:
#     print("não ha", x, "na lista animal")
#     lista_animal.append(x)
#     print(lista_animal)
