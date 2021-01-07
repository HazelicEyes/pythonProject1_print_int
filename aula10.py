from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))

    dias = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Zoro perdido no domingo")
    print(dias[data_atual.weekday()])
    

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%y')) #formatar a data
    print(data_atual.strftime('%A %B %Y')) #formatar dia

    data_atual_str = data_atual.strftime('%A %B %Y') #convertido
    print(data_atual_str)

def trabalhando_com_time():
    horario = time(hour=11, minute=22, second=33)
    print(horario)
    print(type(horario))

    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))




if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()