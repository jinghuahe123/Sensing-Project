import main_playback as play

def main(duration, f0, f1):
    play.play_chirp(duration, f0, f1)
    play.save_chirp(duration, f0, f1)

if __name__ == "__main__":
    duration = input("Sound Duration: ")
    f0 = input("Start Frequency: ")
    f1 = input("End Frequency: ")

    print(f"Frequency Difference {int(f1)-int(f0)}Hz over {duration} seconds.")

    main(duration, f0, f1)