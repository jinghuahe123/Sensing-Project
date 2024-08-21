import main_playback as play

def main(duration, f0, f1):
    play.chirp(duration, f0, f1)

if __name__ == "__main__":
    duration = input("Sound Duration: ")
    f0 = input("Start Frequency: ")
    f1 = input("End Frequency: ")

    print(f"Frequency Difference {f1-f0} over {duration} seconds.")

    main(duration, f0, f1)