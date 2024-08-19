import main_eight_channel as eightchannel

def run(duration):
    recording = eightchannel.record(duration)
    eightchannel.save('8_channel_recording.wav', recording)

if __name__ == "__main__":
    run(10)
