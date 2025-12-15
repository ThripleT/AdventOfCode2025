from ortools.linear_solver import pywraplp

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
        indicators, buttons_tmp, joltages = read_instruction(instruction)

        buttons = []
        for button in buttons_tmp:
            new_button = [0] * len(joltages)
            for j in button:
                new_button[j] += 1
            buttons.append(new_button[:])
        
        solver = pywraplp.Solver.CreateSolver('SAT')
        x = [solver.IntVar(0, 200, f'x_{i}') for i in range(len(buttons))]
        solver.Minimize(sum(x))
        for d in range(len(joltages)):
            solver.Add(sum(buttons[i][d] * x[i] for i in range(len(buttons))) == joltages[d])
        status = solver.Solve()
        if status == pywraplp.Solver.OPTIMAL:
            min_presses = int(solver.Objective().Value())
            processed_instructions.append(min_presses)
        else:
            # Handle infeasible or other cases
            processed_instructions.append(float('inf'))  # or some error value
        
        print(processed_instructions[-1])
            
    return processed_instructions

def main():
    processed = process_instructions(INSTRUCTIONS)
    total = sum(processed)
    return total

if __name__ == "__main__":
    print(main())