from fourFirst import DIAGRAM, check_diagram

def main():
    diagram = DIAGRAM.copy()
    counter = 0
    while True:
        accessible_positions = check_diagram(diagram)
        if not accessible_positions:
            break
        for y, x in accessible_positions:
            diagram[y] = diagram[y][:x] + 'X' + diagram[y][x+1:]
        counter += len(accessible_positions)
    
    for line in diagram:
        print(line)

    return counter

if __name__ == "__main__":
    print(main())