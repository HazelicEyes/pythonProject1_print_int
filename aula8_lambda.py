contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
sub = lambda a, b : a - b

print(soma(5, 10))
print(sub(5, 10))


calculadora = {
    'soma': lambda a, b: a + b,
    'sub': lambda a, b: a + b,
    'multi': lambda a, b: a * b,
    'divi': lambda a, b: a / b
}

print(type(calculadora))
soma = calculadora['soma']
multi = calculadora['multi']

print("A soma é:", soma(15, 5))
print("A multi é:", multi(10, 4))

