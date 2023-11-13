import numpy as np
import sys

def init(Fs, f):
    duration = 1  # Длительность сигнала
    num_samples = Fs * duration  # Количество отсчетов
    
    t = np.linspace(0, duration, num_samples)
    
    # Генерируем сигнал на выбранной частоте дискретизации
    y = 2 * np.sin(2 * np.pi * f * t + np.pi/6)
    
    dis(y, duration)

    return t, y

def dis(y, duration): 
    # Прямое дискретное преобразование Фурье
    dft_result = np.fft.fft(y)
    
    # Вычисляем ширину спектра
    spectral_width = 2 * np.pi / duration
    
    # Выводим ширину спектра
    print(f"Ширина спектра: {spectral_width} рад/сек")
    
    # Оцениваем объем памяти
    memory_usage = sys.getsizeof(dft_result)
    print(f"Объем памяти для DFT: {memory_usage} байт")

def reverse(y):
    # Прямое дискретное преобразование Фурье
    dft_result = np.fft.fft(y)
    # Обратное дискретное преобразование Фурье
    reconstructed_signal = np.fft.ifft(dft_result)
    return reconstructed_signal