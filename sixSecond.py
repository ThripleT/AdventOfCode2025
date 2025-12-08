MATH_PROBLEMS = open('06-input.txt').read().splitlines()

def solve_problems(problems):
    operators = []
    amounts = []
    amount = 0
    for char in problems[-1]:
        if char in '+*':
            operators.append(char)
            if amount > 0:
                amounts.append(amount)
                amount = 0
        else:
            amount += 1
    amounts.append(amount + 1)
    problem_lines = []
    amount = 0
    for line in problems[:-1]:
        problem_line = []
        for a in amounts:
            problem_line.append(line[amount:amount+a])
            amount += a + 1
        problem_lines.append(problem_line)
        amount = 0
    results = []
    for i in range(len(operators)):
        operator = operators[i]
        if operator == '+':
            result = 0
        elif operator == '*':
            result = 1
        else:
            print(f"Unknown operator: {operator}")
            continue
        values = []
        for ii in range(amounts[i]):
            value = ''
            for line in problem_lines:
                value += line[i][ii]
            values.append(int(value))
        for value in values:
            if operator == '+':
                result += value
            elif operator == '*':
                result *= value
        
        results.append(result)
    return results

def main():
    results = solve_problems(MATH_PROBLEMS)
    sum_results = sum(results)
    return sum_results

if __name__ == "__main__":
    print(main())