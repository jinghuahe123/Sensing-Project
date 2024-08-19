import audio, numpy as np

if __name__ == "__main__":
    a, d = audio.parser('8mic.wav')
    data = d.tolist()
    print(data)
    #for x in range(len(d)):
    #    print d[x],

    audio.plot('8mic.wav', 200000)