"""import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

# Load audio file
audio, sample_rate = sf.read('output.wav')
print(audio)
print(sample_rate)

# Create time axis
time = np.arange(0, len(audio)) / sample_rate
print(time)


# Plot audio signal
plt.plot(time, audio)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()"""


import numpy as np
import soundfile as sf

import pyaudio
import wave
import numpy as np

def record_audio(filename, duration, rate=44100, chunk=1024):
    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    print("Recording...")

    frames = []

    for _ in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Recording finished")

    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

def parse_audio(filename):
    with wave.open(filename, 'rb') as wf:
        n_channels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        framerate = wf.getframerate()
        n_frames = wf.getnframes()
        
        print(f"Channels: {n_channels}")
        print(f"Sample Width: {sampwidth}")
        print(f"Frame Rate: {framerate}")
        print(f"Number of Frames: {n_frames}")

        audio_frames = wf.readframes(n_frames)
        audio_data = np.frombuffer(audio_frames, dtype=np.int16)
        
        return audio_data, framerate

def play_audio(filename):
    wf = wave.open(filename, 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(1024)

    while data:
        stream.write(data)
        data = wf.readframes(1024)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf.close()

# Usage example
record_audio("output.wav", 5)  # Record for 5 seconds
audio_data, framerate = parse_audio("output.wav")
print(audio_data[:10])  # Print first 10 audio samples
play_audio("output.wav")
