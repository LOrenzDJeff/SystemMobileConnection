import numpy as np
import transmitter as base
import functions as func

#Генерация шума и передача массива на приёмник
def main():
    signal, length = base.main()
    signal = np.asarray(signal)
    o = float(input("Введите стандратное отклоненние: "))
    noise = np.random.normal(0, o, len(signal))
    signoise = []
    for i in range(len(signal)):
        signoise.append(noise[i] + signal[i])
    func.graphic(signoise, "Сигнал с шумом")
    return signoise, length

main()