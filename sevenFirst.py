FIELD = open('07-input.txt').read().splitlines()

def beam_splitting(field):
    beams = []
    splits = 0
    for line in field:
        if not beams:
            beams.append(line.find('S'))
        else:
            new_beams = []
            for beam in beams:
                if line[beam] == '.':
                    if beam not in new_beams:
                        new_beams.append(beam)
                elif line[beam] == '^':
                    splits += 1
                    if beam - 1 not in new_beams:
                        new_beams.append(beam - 1)
                    if beam + 1 not in new_beams:
                        new_beams.append(beam + 1)
            beams = new_beams.copy()
    return beams, splits

def main():
    beams, splits = beam_splitting(FIELD)
    return beams, splits

if __name__ == "__main__":
    print(main())