import os
import time

def getVals():
    try:
        data = open('metadata', 'r').read().split(",")
        return (int(data[0]), int(data[1]), int(data[2]))
    except:
        print("couldn't get metadata")
        return (None, None, None)
    
def prepareFrames(filename):
    data = open(filename, "r").read().split("\n")
    for i in range(len(data)):
        data[i] = data[i].replace(",", "\n")
    return data

def main():
    (WIDTH, HEIGHT, frames) = getVals()

    startTime = time.time()
    data = prepareFrames("badApple.txt")

    frame = 0

    while frame < frames:
        # os.system('cls')
        if (t:=time.time()) > startTime + (1/30) * frame:
            print(data[frame])
            frame += 1

if __name__ == '__main__':
    main()