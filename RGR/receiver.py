import functions as func
import numpy as np
import radio_channel as rd

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

#8 point
signal, length = rd.main()
golden, G = func.Gold()
golden = np.repeat(golden, 4)
for i in range(len(signal) - len(golden)):
    suma = 0
    for j in range(len(golden)):
        try:
            suma = suma + (golden[j] * signal[i + j])
        except IndexError:
            break
    if i == 0:
        maximum = suma
        pos = 0
    elif maximum < suma:
        maximum = suma
        pos = i 
synsig = []
for i in range(pos, pos + length):
    synsig.append(signal[i])
print(synsig)

#9 point
cipher = []
for i in range(int(len(synsig) / 4)):
    if synsig[i * 4] > 0.5:
        cipher.append(1)
    else:
        cipher.append(0)
        
#10 point
ciphernotgold = []
for i in range(G, len(cipher)):
    ciphernotgold.append(cipher[i])
    
#11 point
CRC = func.CRC(ciphernotgold)
print(CRC)

#12point
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