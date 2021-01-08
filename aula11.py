
lista = [1, 10]


try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]


except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except IndexError:
    print("IndexError")
except Exception as ex:
    print("erro desconhecido. \nErro:",ex)
else:
    print("executa quando nao houve erro")

finally:
    print("no finally sempre vai ser executado. \nfechando arquivo...")
    arquivo.close()