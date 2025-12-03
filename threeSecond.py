import numpy as np

BANKS = open("03-input.txt").readlines()

def get_highest_number(bank, lenght):
    digits = np.zeros(lenght, dtype=int)
    for i, digit in enumerate(bank):
        changed = False
        for ii, d in enumerate(digits):
            if changed:
                digits[ii] = 0
                continue
            if ii <= i <= len(bank) - (lenght - ii):
                if int(digit) > d:
                    digits[ii] = int(digit)
                    changed = True
                    continue

    number = ''.join(map(str, digits))
    return int(number)

def main():
    total = 0

    for bank in BANKS:
        bank = bank.strip()
        total += get_highest_number(bank, 12)

    return total

if __name__ == "__main__":
    print(main())