import threading, main_eight_channel as eightchannel, main_playback as play

def main(duration, f0, f1, sample_rate=48000, channels=8):

    def threading_record():
        global recording
        recording = eightchannel.record(duration, sample_rate, channels)
        
    play_thread = threading.Thread(target=play.play_chirp, args=(duration, f0, f1, sample_rate))
    record_thread = threading.Thread(target=threading_record)

    record_thread.start()
    play_thread.start()

    record_thread.join()
    play_thread.join()

    play.save_chirp(duration, f0, f1, sample_rate)
    eightchannel.save("recorded_signal.wav", recording, sample_rate)
    eightchannel.plot("recorded_signal.wav")

if __name__ == "__main__":
    duration = input("Duration: ")
    f0 = input("Start Frequency: ")
    f1 = input("End Frequency: ")

    main(duration, f0, f1)

    