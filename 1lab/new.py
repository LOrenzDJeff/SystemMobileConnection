from scipy import signal
import sounddevice as sd

def newvoice(audio, sample_rate, new_sample_rate):
    # Изменение частоты дискретизации
    resampled_audio = signal.resample(audio, int(len(audio) * new_sample_rate / sample_rate))
    # Воспроизведение аудио с новой частотой дискретизации
    sd.play(resampled_audio, new_sample_rate)
    sd.wait()
    return resampled_audio
