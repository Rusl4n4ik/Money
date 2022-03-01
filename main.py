value = {'1': {'Sum':10865, 'Euro': 0.89, 'Rub': 83.82},
         '2': {'Dollar': 0.012, 'Euro': 0.011, 'Sum': 129.62},
         '3': {'Dollar': 1.13, 'Rub': 94.50, 'Sum': 12249.20},
         '4': {'Dollar': 0.000092, 'Euro': 0.000082, 'Rub': 0.0077}
         }

#1-Dollar, 2-Rub, 3-Euro, 4-Sum


def pidr(value1, value1_c, value2):
    return value[value1][value2] * value1_c


class Sum:

    def vl(self):
        __index = 1
        try:
            value1 = input(" 1.Доллар\n 2.Евро\n 3.Рубль\n 4.Сум\n Выберите валюту: ")
            value1_c = int(input("Введите значение: "))
        except KeyError:
            print("Введите верный ключ")
        for Value in value[value1]:
            print(str(__index) + '.' + Value)
            __index += 1
        value2 = input("Выберите валюту: ")
        value[value1][value2]
        print(pidr(value1,value1_c,value2))



A = Sum()
A.vl()





