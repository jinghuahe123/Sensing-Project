import main_eight_channel as eightchannel

duration = 6

def main():
    #recording = eightchannel.record(duration, channels=6)
    #eightchannel.save('eightchannel.wav', recording)

    eightchannel.plot('eightchannel.wav')

if __name__ == "__main__":
    main()