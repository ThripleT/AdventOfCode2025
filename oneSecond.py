import oneFirst

def main():
    position = oneFirst.START_POSITION
    counter = 0

    for instructor in oneFirst.INSTRUCTIONS:
        rotation = int(instructor[1:].removesuffix('\n'))
        while rotation > 100:
            counter += 1
            rotation -= 100
        if instructor[0] == 'L':
            rotation *= -1
        position += rotation

        if not -1 < position < 100:
            counter += 1
        
        position %= 100
    
    return counter

if __name__ == "__main__":
    print(main())
