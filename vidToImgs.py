import cv2

WIDTH = int(5/3 * 60)
HEIGHT = 35

def logMeta(frames):
    log = open("metadata", "w")
    log.write(f'{WIDTH},{HEIGHT},{frames}')
    log.close()

def writeAscii(chars):
    file = open("badApple.txt", "w")
    file.write("\n".join(chars))
    file.close()

def toChar(greyVal):
    if greyVal > 183:
        return '@'
    elif greyVal > 128:
        return '*'
    elif greyVal:
        return '.'
    else:
        return ' '

def main():
    capture = cv2.VideoCapture("badApple.mp4")
    success, frame = capture.read()
    count = 0
    chars=[]

    while success:
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rs = cv2.resize(grey, (WIDTH, HEIGHT), interpolation = cv2.INTER_AREA)
        chars.append(",".join(["".join([toChar(p) for p in l]) for l in rs]))

        success, frame = capture.read()
        count += 1
    
    writeAscii(chars)
    logMeta(count)


if __name__ == '__main__':
    main()