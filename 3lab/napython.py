import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 100)
pi = 3.14

s1 = np.cos(2 * pi * t * 1)
s2 = np.cos(2 * pi * t * 5)
s3 = np.cos(2 * pi * t * 3)
a = 2 * s1 + 4 * s2 + s3
b = s1 + s2

corsa = np.sum(s1 * a)
corsb = np.sum(s1 * b)
print("Корреляция a s1")
print(corsa)
print("Корреляция b s1")
print(corsb)

multa = 0
multb = 0
mults = 0

for n in range(100):
    mults = s1[n] * s1[n] + mults
    multa = a[n] * a[n] + multa
    multb = b[n] * b[n] + multb

cornormsa = corsa / np.sqrt(mults * multa)
cornormsb = corsb / np.sqrt(mults * multb)
print("Нормализованая корреляция a s1")
print(cornormsa)
print("Нормализованая корреляция b s1")
print(cornormsb)

a = [0.3, 0.2, -0.1, 4.2, -2, 1.5, 0]
b = [0.3, 4, -2.2, 1.6, 0.1, 0.1, 0.2]
corab = np.sum(np.array(a) * np.array(b))
print("Корреляция a b")
print(corab)

fig, axs = plt.subplots(5, 1, figsize=(8, 20))

axs[0].plot(a)
axs[0].set_title("a = [0.3 0.2 -0.1 4.2 -2 1.5 0]")

axs[1].plot(b)
axs[1].set_title("b = [0.3 4 -2.2 1.6 0.1 0.1 0.2]")

maxsdvig = 0
maxznach = corab
cormas = np.zeros(len(a))
cormas[0] = corab

for shift in range(1, len(cormas)):
    save1 = b[0]
    b[0] = b[-1]
    for dvij in range(1, len(b)):
        save2 = b[dvij]
        b[dvij] = save1
        save1 = save2
    corab = np.sum(np.array(a) * np.array(b))
    if corab > maxznach:
        maxznach = corab
        maxsdvig = shift
    cormas[shift] = corab

for i in range(maxsdvig + 1):
    save1 = b[0]
    b[0] = b[-1]
    for dvij in range(1, len(b)):
        save2 = b[dvij]
        b[dvij] = save1
        save1 = save2

print("Максимальная корреляция")
print(maxznach)
print("При сдвиге")
print(maxsdvig)
axs[2].plot(a)
axs[2].set_title("a = [0.3 0.2 -0.1 4.2 -2 1.5 0]")

axs[3].plot(b)
axs[3].set_title("b со сдвигом")

axs[4].plot(cormas)
axs[4].set_title("Корреляция со сдвигом b")

plt.show()
