import sounddevice as sd, numpy as np, scipy.io.wavfile as wav, matplotlib.pyplot as plt

# record audio
def record(duration, sample_rate=48000, channels=8):
    print(f"Recording {channels}-channel audio for {duration} seconds...")
    recording = sd.rec(
        int(sample_rate * duration), 
        samplerate=sample_rate, 
        channels=channels, 
        dtype='int16'
        )
    sd.wait() 
    return recording

# save the recording as .wav
def save(filename, recording, sample_rate=48000):
    recording = recording / np.max(np.abs(recording), axis=0) # normalize recording to [-1, 1]
    wav.write(filename, sample_rate, recording)
    print(f"Recording saved as {filename}")

# read .wav
def read(filename):
    sample_rate, data = wav.read(filename)
    
    print(f"Sample Rate: {sample_rate} Hz")
    print("Raw Data:")
    print(data)

# plot on graph
def plot(filename):
    sample_rate, data = wav.read(filename)
    
    channels = data.shape[1]
    time = [i / sample_rate for i in range(data.shape[0])] # time axis

    # plot each channel
    fig, axs = plt.subplots(channels, 1, figsize=(10, 2 * channels))
    fig.suptitle(f'Audio Channels from {filename}')

    for i in range(channels):
        axs[i].plot(time, data[:, i])
        axs[i].set_title(f'Channel {i + 1}')
        axs[i].set_xlabel('Time [s]')
        axs[i].set_ylabel('Amplitude')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print("This file has no executable function. Please run another file.")
