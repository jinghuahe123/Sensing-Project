from audio import *
import argparse

def parse():
    arg = argparse.ArgumentParser(description="main.py")
    arg.add_argument('-f', choices=["record", "play", "parse", "plot"], required=True, help="Option to select function.")
    arg.add_argument('-t', type=int, help="Recording length.")
    arg.add_argument('-o', type=str, help="Filename.")
    arg.add_argument('-s', type=int, help="Slice output.")

    args = arg.parse_args()

    if args.f in ["record"]:
        if args.t is None or args.o is None:
            arg.error("Recording selected, time and filename required.")
            exit(1)
        else:
            record(args.t, args.o)
    elif args.f in ["play"]:
        if args.o is None:
            arg.error("Playback selected, filename required.")
            exit(1)
        else:
            play(args.o)
    elif args.f in ["parse"]:
        if args.o is None:
            arg.error("Parser selected, filename required.")
            exit(1)
        else:
            audio, data = parser(args.o)
            print(audio[:args.s])
            print(data[:args.s])
    elif args.f in ["plot"]:
        if args.o is None or args.s is None:
            arg.error("Plotting selected, filename and slice required.")
            exit(1)
        else:
            plot(args.o, args.s)
    else:
        arg.error("Invalid arguments.")
        exit(1)

if __name__ == "__main__":
    parse()