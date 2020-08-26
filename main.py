print("Teste de resultados")
a = int(input('Entre o primeiro valor: '))
b = int(input('Entre o segundo valor: '))
soma = a + b
subi = a - b
multi = a * b
divi = a / b
resto = a % b

# use print(type()) ou similar para saber o tipo da variavel etc

print("A é:", a)
print("B é:", b)
print("-------------------------------")
print("A Soma é:", soma)
print("A Subtração é:", subi)
print("A Multiplicação é:", multi)
print("A Divisão é:", divi)
print("O Resto da divisão é:", resto)
print("-------------------------------")
soma2 = a + 99
print(a, "+ 99 é:", soma2)