import main_eight_channel as eightchannel

def run(duration):
    recording = eightchannel.record_audio(duration)
    eightchannel.save_audio('8_channel_recording.wav', recording)

if __name__ == "__main__":
    run(10)
