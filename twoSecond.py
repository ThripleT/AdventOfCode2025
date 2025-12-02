RANGES = open("02-input.txt").read().split(',')

def get_repeats(start, end):
    repeats = []
    for i in range(start, end+1):
        i = str(i)
        lenght = len(i)
        for ii in range(1, int(lenght/2)+1):
            repeat = True
            if lenght % ii != 0:
                continue
            for iii in range(1, int(lenght/ii)):
                for iv in range(ii):
                    if i[iv] != i[iv+iii*ii]:
                        repeat = False
                        break
                if not repeat:
                    break
            if repeat:
                repeats.append(int(i))
                break
    return repeats

def main():
    counter = 0

    for r in RANGES:
        start = int(r.split('-')[0])
        end = int(r.split('-')[1])

        for repeat in get_repeats(start, end):
            counter += repeat

    return counter

if __name__ == "__main__":
    print(main())