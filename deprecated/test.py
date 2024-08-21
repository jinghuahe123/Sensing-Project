import numpy as np
import sounddevice as sd
import time
import scipy.io.wavfile as wav
import sys

# Parameters
duration = 5  # Duration in seconds
sampling_rate = 48000  # Sampling rate in Hz
chirp_start_freq = 4000  # Starting frequency of the chirp in Hz
chirp_end_freq = 5000    # Ending frequency of the chirp in Hz
output_filename = "recorded_audio.wav"  # Output WAV file name

# Generate chirp signal
def generate_chirp(duration, sampling_rate, start_freq, end_freq):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    chirp_signal = np.sin(2 * np.pi * (start_freq + (end_freq - start_freq) * t / duration) * t)
    return chirp_signal

# Callback function to play chirp and record audio simultaneously
def callback(indata, outdata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    # Play the chirp signal
    outdata[:] = chirp_signal[:frames].reshape(-1, 1)
    # Record the input audio
    recorded_audio.append(indata.copy())

# Generate chirp signal
chirp_signal = generate_chirp(duration, sampling_rate, chirp_start_freq, chirp_end_freq)

# Prepare a list to store recorded audio data
recorded_audio = []

# Open audio stream
with sd.Stream(channels=2, callback=callback, samplerate=sampling_rate, blocksize=int(sampling_rate*duration)) as stream:
    print("Recording and playing chirp...")
    time.sleep(duration)

# Convert the list of numpy arrays into a single numpy array
recorded_audio = np.concatenate(recorded_audio, axis=0)

# Normalize the recorded audio (optional, depending on your needs)
recorded_audio = recorded_audio / np.max(np.abs(recorded_audio))

# Save the recorded audio to a WAV file
wav.write(output_filename, sampling_rate, recorded_audio.astype(np.float32))

print(f"Finished recording and playing chirp. Audio saved to {output_filename}.")
