class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True: #loop
    try:
        x = int(input("manda um numero de 0 a 10 pro pai ai:"))
        print(x)
        if x > 10:
            raise InputError('maior que 10 nao ne pai')
        elif x < 0:
            raise InputError('menor que 0 nao ne pai')
        break
    except ValueError:
        print("valor invalido, tem q ser numero ne o krl")
    except InputError as ex:
        print(ex)