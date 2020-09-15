class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
    def power(self):
        if self.ligada == True:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada == True:
            self.canal += 1
    def diminui_canal(self):
        if self.ligada == True:
            self.canal -= 1

print(__name__)
if __name__ == '__main__':
    televisao = Televisao()
    print("Televisao esta ligada: {}".format(televisao.ligada))

    televisao.power()
    print("Televisao esta ligada: {}".format(televisao.ligada))


    print("Canal: {}".format(televisao.canal))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print("Canal: {}".format(televisao.canal))
    televisao.diminui_canal()
    print("Canal: {}".format(televisao.canal))

    televisao.power()
    print("Televisao esta ligada: {}".format(televisao.ligada))