import numpy as np
import matplotlib.pyplot as plt
import mathematic as mt
import ocifr as ocf

%matplotlib

f = 10  # Частота сигнала
t = np.linspace(0, 1, 1000)  #1000 точек на интервале от 0 до 1 секунды

# Генерация сигнала
y = 2 * np.sin(2 * np.pi * f * t + np.pi/6)


max_frequency = mt.maxspectre(y)
Fs_min = 4 * mt.Kotelnikov(f)
t2, y_mas = ocf.init(Fs_min, f)
reconstructed_signal = ocf.reverse(y_mas)

# Визуализация сигнала
plt.figure(figsize=(10, 4))
plt.subplot(2, 1, 1)
plt.plot(t, y)
plt.title("Непрерывный сигнал y(t) = 2sin(2*pi*5*t + pi/6)")
plt.xlabel("Время (секунды)")
plt.ylabel("Амплитуда")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t2, reconstructed_signal)
plt.title('Восстановленный сигнал')
plt.xlabel('Время (секунды)')
plt.ylabel('Амплитуда')
plt.grid(True)

plt.tight_layout()
plt.show()