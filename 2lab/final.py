import numpy as np
import math as mt
import matplotlib.pyplot as plt
%matplotlib
# Определение констант и параметров
hBS = 50
hBuild = 30
freq = 1.9
TxPowerBS = 43
TxPowerUE = 23
AntGainBS = 21
fi = 35
IM = 6
NoiseFigure1 = 2.4
NoiseFigure2 = 6
RequiredSINRDl = 2
RequiredSINRUl = 4
MIMOGain = 2
PenetrationM = 17
Q1 = 2.4
Q2 = 7

# Вычисление теплового шума
ThermalNoise1 = -174 + 10 * mt.log10(20000000)
ThermalNoise2 = -174 + 10 * mt.log10(10000000)

# Вычисление чувствительности приемника
RxSensUE = NoiseFigure1 + ThermalNoise1 + RequiredSINRDl
RxSensBS = NoiseFigure2 + ThermalNoise2 + RequiredSINRUl

# Вычисление MAPL для UL и DL
MAPL_DL = TxPowerBS + AntGainBS + MIMOGain - IM - PenetrationM - RxSensUE - Q1
MAPL_UL = TxPowerUE + AntGainBS + MIMOGain - IM - PenetrationM - RxSensBS - Q2
print("MAPL_DL="  + str(MAPL_DL))
print("MAPL_UL="  + str(MAPL_UL))

# Создание массивов для хранения данных
arr = np.zeros(3000)
arr2 = np.zeros(3000)
arr3 = np.zeros(3000)
arr4 = np.zeros(3000)

# Функция для расчета потерь в модели 1
def calculate_model1():
    key1 = True
    for i in range(1, 3000):
        path_long = i
        PL = 26 * mt.log10(freq) + 22.7 + 36.7 * mt.log10(path_long)
        arr[i] = PL
        if PL > MAPL_UL and key1:
            R1 = i - 1
            key1 = False
            print(f"Model 1: R1 = {R1}")
    return R1

# Функция для расчета потерь в модели 2
def calculate_model2():
    key = True
    for i in range(1, 3000):
        path_long = i
        a = 3.2 * (mt.log10(11.75 * 4) ** 2) - 4.97
        LClutter = -(2 * (mt.log10(1800 / 28) ** 2) + 5.4)
        s = 44.9 - 6.55 * mt.log10(1800)
        PL = 46.3 + 33.9 * mt.log10(1800) - 13.82 * mt.log10(150) - a + s * mt.log10(i / 1000) + 3
        arr2[i] = PL
        if PL > MAPL_UL and key:
            R = i - 1
            key = False
            print(f"Model 2: R = {R}")
    return R

# Функция для расчета потерь в модели 3
def calculate_model3():
    for i in range(1, 3000):
        path_long = i
        PL = 42.6 + 20 * mt.log10(1.9) + 26 * mt.log10(i)
        arr3[i] = PL

# Функция для расчета потерь в модели 4
def calculate_model4():
    for i in range(1, 3000):
        path_long = i
        L0 = 32.44 + 20 * mt.log10(1.9) + 20 * mt.log10(i)
        if fi < 35 and fi > 0:
            qoef = -10 + 0.354 * fi
        elif fi < 55 and fi >= 35:
            qoef = 2.5 + 0.075 * fi
        elif fi < 90 and fi >= 55:
            qoef = 4.0 - 0.114 * fi
        L2 = -16.9 - 10 * mt.log10(20) + 10 * mt.log10(1.9) + 20 * mt.log10(hBuild - 3) + qoef
        if hBS > hBuild:
            L1_1 = -18 * mt.log10(1 + hBS - hBuild)
            kD = 18
        elif hBS <= hBuild:
            L1_1 = 0
            kD = 18 - 15 * ((hBS - hBuild) / hBuild)
        if hBS <= hBuild and path_long > 500:
            kA = 54 - 0.8 * (hBS - hBuild)
        elif hBS <= hBuild and path_long <= 500:
            kA = 54 - 0.8 * (hBS - hBuild) * path_long / 0.5
        elif hBS > hBuild:
            kA = 54
            kF = -4 + 0.7 * (1.9 / 925 - 1)
        L1 = L1_1 + kA + kD * mt.log10(path_long) + kF * mt.log10(1.9) - 9 * mt.log10(20)
        if L1 + L2 > 0:
            Llnos = L0 + L1 + L2
        elif L1 + L2 <= 0:
            Llnos = L0
        arr4[i] = Llnos

# Функции для вычисления q1_1 и q1_2
def calculate_q1_1(R):
    return 10000000 / (1.95 * (R ** 2))

def calculate_q1_2(R1):
    return 4000000 / (1.95 * (R1 ** 2))

# Расчет потерь в моделях и вывод результатов
R1 = calculate_model1()
R = calculate_model2()
calculate_model3()
calculate_model4()

q1_1 = calculate_q1_1(R)
q1_2 = calculate_q1_2(R1)
dlina = []
for i in range(len(arr)):
    dlina.append(i)
# Построение графиков
plt.figure(figsize=(10, 6))  # Изменение размера графика
plt.minorticks_on()
plt.grid(which='major', color='gray', linestyle='-', linewidth=1)
plt.grid(which='minor', color='gray', linestyle=':', linewidth=0.5)

# Настройка стиля линий и меток для каждого графика
plt.plot(arr, label='UMiNLOS', linestyle='-', color='b')
plt.plot(arr2, label='COST231', linestyle='--', color='g')
plt.plot(arr3, label='Walfish-Ikegami Llos', linestyle='-.', color='r')
plt.plot(arr4, label='Walfish-Ikegami Lnlos', linestyle=':', color='m')
plt.axhline(MAPL_DL, label='MAPL_DL', color='r')
plt.axhline(MAPL_UL, label='MAPL_UL', color='k')

plt.xlabel('Path Length')
plt.ylabel('Path Loss (dB)')
plt.legend()
plt.title('Path Loss Models')
plt.show()