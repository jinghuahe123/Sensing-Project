import pyaudio, wave, numpy as np, matplotlib.pyplot as plt 

def record(duration, filename, format=pyaudio.paInt16, rate=44100, chunk=1024):

    p = pyaudio.PyAudio() # instantiate pyaudio

    stream = p.open(                            # opens a stream
                    format=format,              # how bits are stored, default paInt16 represents signed 16-bit string
                    channels=1,                 # mono audio
                    rate=rate,                  # sampling rate - how many times the sound is sampled in a second
                    input=True,                 # opens a stream for recording not playback
                    frames_per_buffer=chunk     # arbitrarily chosen number of frames signals are split into
                    ) 
    
    
    frames = []

    for _ in range(int(rate / chunk * duration)): # math that calculates the total number of chunks in audio length (rate * duration is total number of frames, divide by number of frames in one chunk)
        data = stream.read(chunk) # takes 1024 (one chunk) of data in each iteration of loop
        frames.append(data)


    stream.stop_stream()
    stream.close()
    p.terminate()


    # convert 'frames' list into wav file with library 'wave'
    with wave.open(filename, 'wb') as wf: # 'wb' is write only mode, 'rb' is read only mode (does not support r/w)
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(format)) # sample width is the number of y-axis steps
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames)) # empty bytestring that 'frames' list is appended to

    wave.close()


def play(filename):

    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()

    stream = p.open(
                    format=p.get_format_from_width(wf.getsampwidth()), # gets samplewidth from wf object
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True
                    )
    
    chunk = 1024
    while data := wf.readframes(chunk): # edited to shorten example code with walrus (see below)
        stream.write(data)

    '''
    data = wf.readframes(1024)

    while data:
        stream.write(data)
        data = wf.readframes(1024)
    '''

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf.close()


def parser(filename, output=True):
    with wave.open(filename, 'rb') as wf:
        nchannels = wf.getnchannels()
        width = wf.getsampwidth()
        rate = wf.getframerate()
        nframes = wf.getnframes()

        if output:
            print(f"Channels: {nchannels}")
            print(f"Sample Width: {width}")
            print(f"Sample Rate: {rate}")
            print(f"Total Frames: {nframes}")

        audio = wf.readframes(nframes)
        data = np.frombuffer(audio, dtype=np.int16)

        return audio, data
    

def plot(filename, slice=None):
    with wave.open(filename, 'rb') as wf:
        nframes = wf.getnframes()
        rate = wf.getframerate()

        audio = wf.readframes(nframes)
        data = (np.frombuffer(audio, dtype=np.int16)).tolist()

    time = np.arange(nframes) / rate

    plt.plot(time[:slice], data[:slice])
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()
    

if __name__ == "__main__":
    #audio, data = parser("一路生花.wav")
    #print(audio)
    #print(data)
    #print(type(audio))

    plot("一路生花.wav", 10000000)

    play("一路生花.wav")