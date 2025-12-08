FIELD = open('07-input.txt').read().splitlines()

def beam_splitting(field):
    beams = []
    splits = 0
    for line in field:
        if not beams:
            beams.append((line.find('S'), 1))
        else:
            new_beams = []
            for beam in beams:
                if line[beam[0]] == '.':
                    new_beams.append(beam)
                elif line[beam[0]] == '^':
                    splits += 1
                    new_beams.append((beam[0] - 1, beam[1]))
                    new_beams.append((beam[0] + 1, beam[1]))
            
            beams.sort()

            beams = []
            last_number = None
            for beam in new_beams:
                if beam[0] == last_number:
                    beams[-1] = (beams[-1][0], beams[-1][1] + beam[1])
                else:
                    beams.append(beam)
                    last_number = beam[0]

    return beams, splits

def main():
    beams, splits = beam_splitting(FIELD)
    timelines = 0
    for beam in beams:
        timelines += beam[1]
    return beams, splits, timelines

if __name__ == "__main__":
    print(main())