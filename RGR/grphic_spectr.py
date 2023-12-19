import functions as func
import numpy as np
from scipy.fft import fftshift, fft
import matplotlib.pyplot as plt

#Повтороение пунктов 1-7 для вывода спектра передаваемого и принимаемого
#(зашумленного) сигналов

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

def main(N):
    #1 point
    name = "Babenko Denis"
    
    #2 point
    kod = coder(name)
    
    #3 point
    M = len(kod)
    delete = [1, 0, 1, 1, 1, 1, 1, 1]
    for i in range(len(delete) - 1):
        kod.append(0)
    CRCnum = func.CRC(kod)
    for i in range(M, len(kod)):
        kod[i] = CRCnum[i - M]
    
    #4 point
    golden, G = func.Gold()
    for i in range(G):
        kod.append(0)
        kod = func.shiftright(kod)  
    for i in range(G):
        kod[i] = golden[i]
    
    #5 point
    signal = np.repeat(kod, N)
    
    #6 point
    bigsignal = [int(0) for i in range(2 * len(signal))]
    key = 120
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
    #first = fftshift(fft(bigsignal))
    
    signal = np.asarray(bigsignal)
    o = 0.15
    noise = np.random.normal(0, o, len(signal))
    signoise = []
    for i in range(len(signal)):
        signoise.append(noise[i] + signal[i])
    
    second = fftshift(fft(signoise[110:500]))
    
    return second

rec = main(2)
man = main(4)
dig = main(8)
#plt.plot(base, "g")
plt.figure()
plt.title("Спектры сигналов")
plt.plot(rec, "g")
plt.plot(man, "r")
plt.plot(dig, "b")
