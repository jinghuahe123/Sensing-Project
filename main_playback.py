import numpy as np, sounddevice as sd
from scipy.signal import chirp

# chirp signal
def gen_chirp(duration, f0, f1, sample_rate=48000):
    t = np.linspace(0, duration, int(sample_rate * duration)) # time array

    signal = chirp(t, f0=f0, f1=f1, t1=duration, method='linear')

    sd.play(signal, sample_rate)
    sd.wait()


if __name__ == "__main__":
    print("This file has no executable function. Please run another file.")
