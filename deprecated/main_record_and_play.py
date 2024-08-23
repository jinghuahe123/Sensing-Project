import sounddevice as sd, numpy as np, main_playback as playback

def play_and_record(duration, f0, f1, sample_rate=48000, channels=2):
    chirp_signal = playback.gen_chirp(duration, f0, f1, sample_rate)
    
    # Initialize an array to store the recording
    recording = np.zeros((int(sample_rate * duration), channels), dtype='int16')
    
    # Define a callback function to handle both playback and recording
    def callback(indata, outdata, frames, time, status):
        outdata[:] = chirp_signal[:frames, np.newaxis]
        recording[:frames] = indata
    
    # Create a stream for simultaneous playback and recording
    with sd.Stream(samplerate=sample_rate, channels=channels, dtype='int16', callback=callback):
        sd.sleep(int(duration * 1000))  # Sleep for the duration of the chirp in milliseconds

    return chirp_signal, recording

if __name__ == "__main__":
    print("This file has no executable function. Please run another file.")
