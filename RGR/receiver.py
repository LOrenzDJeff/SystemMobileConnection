import functions as func
import numpy as np
import radio_channel as rd

#Отдельная функция для декодирования двоичных числа в строчные буквы 
def decoder(code):
    sim = ""
    decode = []
    j = 0
    for i in code:
        if j == 7:
            decode.append(chr(int(sim, 2)))
            j = 0
            sim = ""
        sim += str(i)
        j += 1
    decode.append(chr(int(sim, 2)))
    return decode

#Синхронизация с сигналом и отброс лишних нулей в массиве
signal, length = rd.main()
golden, G = func.Gold()
golden = np.repeat(golden, 4)
autocor = []
for i in range(len(signal) - len(golden)):
    suma = 0
    for j in range(len(golden)):
        try:
            suma = suma + (golden[j] * signal[i + j])
        except IndexError:
            break
    autocor.append(suma)
    if i == 0:
        maximum = suma
        pos = 0
    elif maximum < suma:
        maximum = suma
        pos = i 
print("Автокор: ", maximum)
synsig = []
for i in range(pos, pos + length):
    synsig.append(signal[i])
func.graphic(autocor, "Автокорреляия")
func.graphic(synsig, "Синхросигнал")

#Преобразование временных отсчётов в информацию и избавление от шума
cipher = []
for i in range(int(len(synsig) / 4)):
    if synsig[i * 4] > 0.5:
        cipher.append(1)
    else:
        cipher.append(0)
        
#Удаление последовательности Голда
ciphernotgold = []
for i in range(G, len(cipher)):
    ciphernotgold.append(cipher[i])
    
#Проверка CRC
CRC = func.CRC(ciphernotgold)
print("CRC:", CRC)
if 1 in CRC:
    print("Ошибка CRC")

else:
    
    #Удаление CRC и декодирование битов информации в буквы
    word = []
    for i in range(len(ciphernotgold) - 7):
        word.append(ciphernotgold[i])
    donemas = decoder(word)
    done = ""
    for i in donemas:
        if ord(i) > 65 and ord(i) < 90:
            done += " "
        done += i
    print(done[1:])