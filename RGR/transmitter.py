import numpy as np
import functions as func

#Отдельная функция для кодирования строчных букв в двоичные числа
def coder(text):
    mas = []
    for i in text:
        if i != " ":
            mas.append(ord(i))

    code = []
    for j in mas:
        dvach = str(bin(j))
        for i in range(2, len(dvach)):
            code.append(int(dvach[i]))
    
    return code

def main():
    #Фамилия и имя для передачи
    name = input("Введите имя и фамилию: ")
    
    #Кодирование информации
    kod = coder(name)
    func.graphic(kod, "Кодирование символов")
    
    #Вычисление CRC
    M = len(kod)
    delete = [1, 0, 1, 1, 1, 1, 1, 1]
    for i in range(len(delete) - 1):
        kod.append(0)
    CRCnum = func.CRC(kod)
    print("CRC:", CRCnum)
    for i in range(M, len(kod)):
        kod[i] = CRCnum[i - M]
    
    #Генерация последовательности Голда
    golden, G = func.Gold()
    for i in range(G):
        kod.append(0)
        kod = func.shiftright(kod)  
    for i in range(G):
        kod[i] = golden[i]
    func.graphic(kod, "Кодирование с голдом и CRC")
    
    #Преобразования битов в временные отсчёты сигналов
    otch = 4
    signal = np.repeat(kod, otch)
    func.graphic(signal, "Отсчёты")
    length = len(signal)
    
    #Внесение массива информации в массив нулей
    bigsignal = [int(0) for i in range(2 * len(signal))]
    key = int(input("Введите число для вставки в массив: "))
    while 1 == 1:
        if key > 0 and key < len(signal):
            break
        else:
            print("Недопустимое число, введите ещё раз")
            key = int(input())
    for i in range(len(bigsignal)):
        if i >= key and i - key < len(signal):
            bigsignal[i] = signal[i - key]
        else:
            bigsignal[i] = 0
            
    func.graphic(bigsignal, "Сигнал с передатчика")
    return bigsignal, length
    
main()