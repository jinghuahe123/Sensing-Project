import main_eight_channel as eightchannel

def main(duration, filename, graph=True):
    recording = eightchannel.record(duration)
    eightchannel.save(filename, recording)
    
    if graph==True:
        eightchannel.plot(filename)

if __name__ == "__main__":
    duration = input("Recording Duration: ")
    filename = input("Output Filename: ")

    main(duration, filename)
