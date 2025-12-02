RANGES = open("02-input.txt").read().split(',')

def get_doubles(start, end):
    doubles = []
    for i in range(start, end+1):
        i = str(i)
        lenght = len(i)
        if lenght % 2 != 0:
            continue
        if i[int(lenght/2):] == i[:int(lenght/2)]:
            doubles.append(int(i))
    return doubles

def main():
    counter = 0

    for r in RANGES:
        start = int(r.split('-')[0])
        end = int(r.split('-')[1])

        for double in get_doubles(start, end):
            counter += double

    return counter

if __name__ == "__main__":
    print(main())