import sounddevice as sd, numpy as np, scipy.io.wavfile as wav

# record audio
def record_audio(duration, sample_rate=48000, channels=8):
    print(f"Recording {channels}-channel audio for {duration} seconds...")
    recording = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=channels, dtype='int16')
    sd.wait() 
    return recording

# save the recording as .wav
def save_audio(filename, recording, sample_rate=48000):
    recording = recording / np.max(np.abs(recording), axis=0) # Normalize recording to the range [-1, 1]
    wav.write(filename, sample_rate, recording)
    print(f"Recording saved as {filename}")

if __name__ == "__main__":
    print("This file has no executable function. Please run another file.")
    