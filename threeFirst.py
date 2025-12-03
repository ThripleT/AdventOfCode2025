BANKS = open("03-input.txt").readlines()

def get_highest_number(bank):
    first_digit = -1
    second_digit = -1
    for i, digit in enumerate(bank):
        if i+1 < len(bank):
            if int(digit) > first_digit:
                first_digit = int(digit)
                second_digit = -1
                continue
        if i > 0:
            if int(digit) > second_digit:
                second_digit = int(digit)
    return first_digit * 10 + second_digit

def main():
    total = 0

    for bank in BANKS:
        bank = bank.strip()
        total += get_highest_number(bank)

    return total

if __name__ == "__main__":
    print(main())