import numpy as np

def maxspectre(y):
    #Прямое дискретное преобразование Фурье
    fft_result = np.fft.fft(y)
    freq = np.fft.fftfreq(len(fft_result))
    magnitude = np.abs(fft_result)
    # Определение максимальной частоты в спектре
    max_frequency = freq[np.argmax(magnitude)]
    print("Максимальная частота в спектре:", max_frequency)
    return max_frequency

def Kotelnikov(f):
    Fs_min = 2 * f
    print("Минимальная необходимая частота дискретизации:", Fs_min, "Герц")
    return Fs_min