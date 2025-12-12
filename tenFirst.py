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

def process_instructions(instructions):
    processed_instructions = []
    for instruction in instructions:
        indicators, buttons, joltages = read_instruction(instruction)
    
        possibilities = []
        for i in range(1, int(math.exp2(len(buttons)))):
            possibility = bin(i)[2:]
            while len(possibility) < len(buttons):
                possibility = '0' + possibility
            possibilities.append(possibility)
        
        machine_indicators = []
        for _ in range(len(indicators)):
            machine_indicators.append('.')

        valid = []
        for possibility in possibilities:
            machine_indicators_tmp = machine_indicators[:]
            for i, button in enumerate(buttons):
                if possibility[i] == '1':
                    for toggle in button:
                        if machine_indicators_tmp[int(toggle)] == '.':
                            machine_indicators_tmp[int(toggle)] = '#'
                        else:
                            machine_indicators_tmp[int(toggle)] = '.'
            if tuple(machine_indicators_tmp) == indicators:
                valid.append((possibility, sum(map(int, possibility))))
        
        #print(f"Valid possibilities for instruction '{instruction}': {valid}")

        processed_instructions.append(sorted(valid, key=lambda x: x[1])[0])
            
    return processed_instructions

def main():
    processed = process_instructions(INSTRUCTIONS)
    total = sum(int(x[1]) for x in processed)
    return total

if __name__ == "__main__":
    print(main())