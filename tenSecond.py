import math

INSTRUCTIONS = open('10-input.txt').read().splitlines()

def read_instruction(instruction):
    indicators = None
    buttons = []
    joltages = None
    for i in instruction.split():
        if i.startswith('['):
            indicators = tuple(i.strip('[]'))
            continue
        if i.startswith('('):
            buttons.append(tuple(map(int, i.strip('()').split(','))))
            continue
        if i.startswith('{'):
            joltages = tuple(map(int, i.strip('{}').split(',')))
            continue
    return indicators, buttons, joltages

def create_possibilities(buttons, depth, estimate=0):
    possibilities = []
    for i in range(buttons[0][1]+1):
        if estimate + i <= buttons[0][1]:
            if depth > 0:
                for possibility in create_possibilities(buttons, depth-1, estimate+i):
                    possibilities.append([i]+possibility)
            else:
                possibilities.append([i])
        else:
            break
    return possibilities

def analyse_loop(joltages, buttons, m_joltages, counter=0, possible_counter_tmp=[], depth=0):
    machine_joltages = m_joltages[:]
    possible_counter = possible_counter_tmp[:]

    while True:
        max_presses = []
        for button in buttons:
            lowest = float('inf')
            lowest_joltage = None
            for j in button:
                if joltages[j] - machine_joltages[j] == 0:
                    lowest = float('inf')
                    break
                elif joltages[j] - machine_joltages[j] < lowest and joltages[j] - machine_joltages[j] > 0:
                    lowest = joltages[j] - machine_joltages[j]
                    lowest_joltage = j
            if lowest != float('inf'):
                max_presses.append((button, lowest, lowest_joltage))
        max_presses = sorted(max_presses, key=lambda x: x[1])

        if not max_presses:
            if tuple(machine_joltages) == joltages:
                possible_counter.append(counter)
            if possible_counter:
                return sorted(possible_counter)[0]
            else:
                return float('inf')
        if len(max_presses) == 1 or max_presses[0][1] != max_presses[1][1]:
            for j in max_presses[0][0]:
                machine_joltages[j] += max_presses[0][1]
            counter += max_presses[0][1]
        else:
            break

    next_buttons = []
    next_joltage = max_presses[0][2]
    for button in max_presses:
        if button[2] == next_joltage:
            next_buttons.append(button)

    possibilities_tmp = create_possibilities(next_buttons, len(next_buttons)-1)

    possibilities = []
    for possibility in possibilities_tmp:
        if len(possibility) == len(next_buttons):
            if sum(possibility) == next_buttons[0][1]:
                possibilities.append(possibility[:])

    for number, possibility in enumerate(possibilities):
        if depth == 0:
            print(number, '/', len(possibilities))
        machine_joltages_tmp = machine_joltages[:]
        for i, button in enumerate(next_buttons):
            for j in button[0]:
                machine_joltages_tmp[j] += possibility[i]
            counter += possibility[i]

        if tuple(machine_joltages_tmp) == joltages:
            possible_counter.append(counter)
            continue
        elif sum(machine_joltages_tmp) > sum(joltages):
            continue
        else:
            p_counter = analyse_loop(joltages, buttons, machine_joltages_tmp, counter, possible_counter, depth=depth+1)
            possible_counter += [p_counter]

    return sorted(possible_counter)[0]

def process_instructions(instructions):
    processed_instructions = []
    for instruction in instructions:
        indicators, buttons, joltages = read_instruction(instruction)

        machine_joltages = []
        for _ in range(len(joltages)):
            machine_joltages.append(0)
        
        possible_counter = analyse_loop(joltages, buttons, machine_joltages)
        print(possible_counter, len(joltages))
        input()

        processed_instructions.append(possible_counter)
            
    return sorted(processed_instructions)

def main():
    processed = process_instructions(INSTRUCTIONS)
    total = sum(int(x[1]) for x in processed)
    return total

if __name__ == "__main__":
    print(main())