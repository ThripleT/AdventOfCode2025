DIAGRAM = open('04-input.txt').read().splitlines()
GRID = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
)

def check_diagram(diagram):
    accessible = []
    for y, line in enumerate(diagram):
        for x, char in enumerate(line):
            if char == '@':
                counter = 0
                for dy, dx in GRID:
                    if 0 <= y+dy < len(diagram) and 0 <= x+dx < len(line):
                        if diagram[y+dy][x+dx] == '@':
                            counter += 1
                if counter < 4:
                    accessible.append((y, x))
    return accessible

def main():
    accessible_positions = check_diagram(DIAGRAM)
    return len(accessible_positions)

if __name__ == "__main__":
    print(main())