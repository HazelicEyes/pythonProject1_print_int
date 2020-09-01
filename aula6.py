conjunto = {1,2,3,4,5}
conjunto2 = {5,6,7,8,9}
##conjunto.discard(1)
print(conjunto)
print(conjunto2)

conjunto_uniao = conjunto.union(conjunto2)
print("União: ", conjunto_uniao)

conjunto_inter = conjunto.intersection(conjunto2)
print("Intersecção: ", conjunto_inter)

conjunto_difer1 = conjunto.difference(conjunto2)
conjunto_difer2 = conjunto2.difference(conjunto)
print("Diferenças1: ", conjunto_difer1)
print("Diferenças2: ", conjunto_difer2)

conjunto_diff_simm = conjunto.symmetric_difference(conjunto2)
print("Simetrica: ", conjunto_diff_simm)

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
conjunto_superset = conjunto_a.issuperset(conjunto_b)
print("A é subconjunto de B: ",conjunto_subset)
print("A é superconjunto de B: ",conjunto_superset)

lista = ["a", "a", "b", "b", "c"]
print(lista)
conjunto_lista = set(lista)
print(conjunto_lista)
lista_conjunto = list(conjunto_lista)
print(lista_conjunto)


# conjunto = {1, 2, 3, 4}
# conjunto.add(5)
# conjunto.discard(2)
# print(type(conjunto))
# print(conjunto)