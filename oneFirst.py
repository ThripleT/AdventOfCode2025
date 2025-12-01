NUMBERS = 99
START_POSITION = 50
INSTRUCTIONS = open("01-input.txt").readlines()

def main():
    position = START_POSITION
    counter = 0

    for instructor in INSTRUCTIONS:
        rotation = int(instructor[1:].removesuffix('\n'))
        if instructor[0] == 'L':
            rotation *= -1
        position = (position + rotation) % 100

        if position == 0:
            counter += 1
    
    return counter

if __name__ == "__main__":
    print(main())