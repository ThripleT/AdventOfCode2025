MATH_PROBLEMS = open('06-input.txt').read().splitlines()

def solve_problems(problems):
    operators = problems[-1].split()
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
        for ii in range(len(problems)-1):
            if operator == '+':
                result += int(problems[ii].split()[i])
            elif operator == '*':
                result *= int(problems[ii].split()[i])
        results.append(result)
    return results

def main():
    results = solve_problems(MATH_PROBLEMS)
    sum_results = sum(results)
    return sum_results

if __name__ == "__main__":
    print(main())