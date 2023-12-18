import matplotlib.pyplot as plt
import numpy as np

#Функция для построения графика
def graphic(mas, title):
    bukashka = np.asarray(mas)
    plt.figure()
    plt.title(title)
    plt.plot(bukashka)

#Реализация CRC
def CRC(pack):
    delete = [1, 0, 1, 1, 1, 1, 1, 1]
    ost = [i for i in range(len(delete))]
    for i in range(len(delete) - 1):
        ost[i] = pack[i + 1] ^ delete[i + 1]
    ost[len(delete) - 1] = pack[len(delete)]
    
    for i in range(len(delete) + 1, len(pack)):
        if(ost[0] != 0):
            for j in range(len(delete) - 1):
                ost[j] = ost[j + 1] ^ delete[j + 1]
        else:
            for j in range(len(delete) - 1):
                ost[j] = ost[j + 1]
        ost[len(delete) - 1] = pack[i]
    
    if(ost[0] != 0):
        for j in range(len(delete)):
            ost[j] = ost[j] ^ delete[j]
    itog = []
    for i in range(1, len(ost)):
        itog.append(ost[i])
    return itog
    
#Сдвиг вправо
def shiftright(mas):
    temp = mas[len(mas) - 1]
    for i in range(len(mas) - 1, 0, -1):
        mas[i] = mas[i - 1]
    mas[0] = temp
    return mas

#Функция для генерации послеовательности Голда
def Gold():
    x = [1, 0, 0, 0, 0]
    y = [0, 0, 0, 1, 0]
    G = 31
    itog = []
    for i in range(G):
        summatorx = x[2] ^ x[3]
        summatory = y[2] ^ y[1]
        itog.append(x[4] ^ y[4])
        x = shiftright(x)
        y = shiftright(y)
        x[0] = summatorx
        y[0] = summatory
    return itog, G