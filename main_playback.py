import numpy as np, sounddevice as sd
from scipy.signal import chirp
from scipy.io.wavfile import write

# generate chirp signal
def gen_chirp(duration, f0, f1, sample_rate):
    duration=int(duration)
    t = np.linspace(0, duration, int(sample_rate * duration)) # time array
    signal = chirp(t, f0=f0, f1=f1, t1=duration, method='linear')

    return signal

# play chirp 
def play_chirp(duration, f0, f1, sample_rate=48000):

    sd.play(gen_chirp(duration, f0, f1, sample_rate), sample_rate)
    sd.wait()

# save chirp to file
def save_chirp(duration, f0, f1, sample_rate=48000):
    signal = gen_chirp(duration, f0, f1, sample_rate)

    signal = np.int16(signal / np.max(np.abs(signal)) * 32767) # normalize to int16

    filename = "chirp_signal_" + f0 + "-" + f1 + "Hz_" + duration + "sec" + ".wav"
    write(filename, sample_rate, signal)

if __name__ == "__main__":
    print("This file has no executable function. Please run another file.")
