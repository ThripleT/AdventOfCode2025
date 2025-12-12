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

def process_loop(buttons, machine_joltages_tmp, counter, valid, joltages, used_button, best=None, memo={}):
    # Shared best-known solution for pruning. best is a single-element list [value].
    if best is None:
        best = [float('inf')]
    
    if tuple(machine_joltages_tmp) in memo.keys():
        if counter >= memo[tuple(machine_joltages_tmp)][0] and frozenset(used_button) == memo[tuple(machine_joltages_tmp)][1]:
            return valid, memo
    
    memo[tuple(machine_joltages_tmp)] = (counter, frozenset(used_button))

    # If current counter already exceeds known best, prune this branch.
    if counter >= best[0]:
        return valid, memo

    max_presses = []
    for button in buttons:
        if button in used_button:
            continue
        lowest = (float('inf'), 0)
        for j in button:
            if joltages[j] - machine_joltages_tmp[j] == 0:
                lowest = (float('inf'), 0)
                break
            elif joltages[j] - machine_joltages_tmp[j] < lowest[0] and joltages[j] - machine_joltages_tmp[j] > 0:
                lowest = (joltages[j] - machine_joltages_tmp[j], j)
        max_presses.append((button, lowest[0], lowest[1]))
    max_presses = sorted(max_presses, key=lambda x: x[1])
    new_valid = valid[:]
    #print(max_presses, used_button)
    if not max_presses:
        return new_valid, memo
    # For each available button, try pressing it 0..lowest times and recurse
    for btn, lowest_val, _idx in max_presses:
        if lowest_val == float('inf'):
            continue
        for i in range(lowest_val + 1):
            new_counter = counter
            new_machine_joltages_tmp = machine_joltages_tmp[:]
            for j in btn:
                new_machine_joltages_tmp[j] += i
            new_counter += i
            # prune if we've already exceeded best
            if new_counter >= best[0]:
                continue

            new_valid = process_loop(buttons, new_machine_joltages_tmp, new_counter, new_valid, joltages, used_button + [btn], best, memo=memo)
            # if applying i presses already reaches the target, record that cost
            if tuple(new_machine_joltages_tmp) == joltages:
                new_valid.append(new_counter)
                if new_counter < best[0]:
                    best[0] = new_counter
        break
    if tuple(machine_joltages_tmp) == joltages:
        print(new_valid)
        new_valid.append(counter)
    return new_valid, memo

def process_instructions(instructions):
    global one
    processed_instructions = []
    for instruction in instructions:
        indicators, buttons, joltages = read_instruction(instruction)
        
        machine_joltages = []
        for _ in range(len(joltages)):
            machine_joltages.append(0)
        
        counter = 0
        while True:
            max_presses = []
            for button in buttons:
                lowest = (float('inf'), 0)
                for j in button:
                    if joltages[j] - machine_joltages[j] == 0:
                        lowest = (float('inf'), 0)
                        break
                    elif joltages[j] - machine_joltages[j] < lowest[0] and joltages[j] - machine_joltages[j] > 0:
                        lowest = (joltages[j] - machine_joltages[j], j)
                max_presses.append((button, lowest[0], lowest[1]))
            
            max_presses = sorted(max_presses, key=lambda x: x[1])

            if max_presses[0][1] == max_presses[1][1]:
                break
            else:
                for j in max_presses[0][0]:
                    machine_joltages[j] += max_presses[0][1]
                counter += max_presses[0][1]
                
        #print(max_presses, counter)
        valid = []
        valid = process_loop(buttons, machine_joltages, counter, valid, joltages, [])

        processed_instructions.append(sorted(valid, key=lambda x: x)[0])
        print(processed_instructions[-1])
            
    return processed_instructions

def main():
    processed = process_instructions(INSTRUCTIONS)
    total = sum(int(x) for x in processed)
    return total

if __name__ == "__main__":
    print(main())