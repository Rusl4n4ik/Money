value = {'1': {'1':10865, '2': 0.89, '3': 83.82},
         '2': {'1': 0.012, '2': 0.011, '3': 129.62},
         '3': {'1': 1.13, '2': 94.50, '3': 12249.20},
         '4': {'1': 0.000092, '2': 0.000082, '3': 0.0077}
         }

# 1-Dollar, 2-Rub, 3-Euro, 4-Sum
# 1: 1-Sum, 2-Euro, 3-Rub
# 2: 1- Dollar, 2-Euro, 3-Sum
# 3: 1-Dollar, 2-Rub, 3-Sum
# 4: 1-Dollar, 2-Euro, 3-Rub


def pidr(value1, value1_c, value2):
    return value[value1][value2] * value1_c


class Sum:

    def vl(self):
        try:
            value1 = input(" 1.Доллар\n 2.Евро\n 3.Рубль\n 4.Сум\n Выберите валюту: ")
            value1_c = int(input("Введите значение: "))
        except KeyError:
            print("Введите верный ключ")
        value2 = input("Выберите валюту: ")
        value[value1][value2]
        print(pidr(value1,value1_c,value2))



A = Sum()
A.vl()





