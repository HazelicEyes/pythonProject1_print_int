print("Calculo de media do aluno\n")
a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input("Voce digitou errado. Primeiro bimestre:"))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input("Voce digitou errado. Segundo bimestre:"))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input("Voce digitou errado. Terceiro bimestre:"))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input("Voce digitou errado. Quarto bimestre:"))
media = (a + b + c + d) / 4
print("\nSua media é: {}".format(media))
if media >= 6:
    print("Aluno aprovado fodase")
else:
    print("Aluno reprovadokkkkkkkkkkkk")














# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or not resto_b > 0:
#     print("tem numero par")
# else:
#     print("nao tem numero par")

# a = int(input("Primeiro valor: "))
# b = int(input("Segundo valor: "))
# c = int(input("Terceiro valor: "))
#
# if a > b and a > c:
#     print("O maior numero é: {}" .format(a))
# elif b > a and b > c:
#     print("O maior numero é: {}" .format(b))
# else:
#     print("O maior numero é: {}".format(c))
# print('Final do programa')