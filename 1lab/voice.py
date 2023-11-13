import librosa
import numpy as np
import new
import matplotlib.pyplot as plt

%matplotlib

audio_path = 'voice.wav'
original_audio, sample_rate = librosa.load(audio_path)

# Извлечение основных характеристик аудиозаписи
duration = librosa.get_duration(y=original_audio, sr=sample_rate)
num_samples = len(original_audio)
num_channels = original_audio.shape[0]
frame_rate = sample_rate

# Вывод информации о файле
print(f"Длительность аудиозаписи: {duration} секунд")
print(f"Количество выборок: {num_samples}")
print(f"Количество каналов: {num_channels}")
print(f"Частота дискретизации: {frame_rate} Гц")

# вычисление спектрограммы
spectrogram = np.abs(librosa.stft(original_audio))
print("Размер спектрограммы:", spectrogram.shape)

new_sample_rate = 16000
resampled = new.newvoice(original_audio, sample_rate, new_sample_rate)

dft_original = np.fft.fft(original_audio)
dft_resampled = np.fft.fft(resampled)

original_spec = np.abs(np.fft.fft(original_audio))
resampled_spec = np.abs(np.fft.fft(resampled))

# Вычисление частот для амплитудного спектра
n = len(original_spec)
freq = np.fft.fftfreq(n, 1 / sample_rate)

freq1 = np.fft.fftfreq(len(resampled_spec), 1 / new_sample_rate)

# Определение ширины спектра
# Например, можно найти половину максимальной амплитуды
half_max_amplitude = np.max(original_spec) / 2
indices = np.where(original_spec > half_max_amplitude)
width = np.max(freq[indices]) - np.min(freq[indices])

# Вывод амплитудных спектров и ширины спектра
plt.figure(figsize=(10, 6))
plt.plot(freq, original_spec, label='Оригинальный сигнал', color='blue')
plt.plot(freq1, resampled_spec, label='Прореженный сигнал', color='red')
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда')
plt.title('Амплитудные спектры оригинального и прореженного сигналов')
plt.legend()
plt.grid()
plt.show()

print(f"Ширина спектра оригинального сигнала: {width} Гц")  
#new.graphs(original_audio, sample_rate, resampled)