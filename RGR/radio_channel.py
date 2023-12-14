import numpy as np
import transmitter as base
import functions as func

def main():
    signal, length = base.main()
    signal = np.asarray(signal)
    o = 0.1
    noise = np.random.normal(0, o, len(signal))
    signoise = []
    for i in range(len(signal)):
        signoise.append(noise[i] + signal[i])
    func.graphic(signoise, "7")
    return signoise, length

main()