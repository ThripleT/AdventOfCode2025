CONNECTIONS = {}
STEPS = ['dac', 'fft']
START = 'svr'
END = 'out'

for line in open('11-input.txt').read().splitlines():
    connection = line.split()
    CONNECTIONS[connection[0].removesuffix(':')] = connection[1:]

def get_out(start:str, end:str, steps:list=[], paths:dict={}, current_path:list=[], return_counter:bool=False):
    counter = 0
    if start in current_path:
        try:
            return paths.copy(), paths[start]
        except KeyError:
            return paths.copy(), 0
    for connection in CONNECTIONS[start]:
        if connection in steps:
            steps.remove(connection)
        if connection == end:
            if not steps:
                counter += 1
                if connection in paths.keys():
                    paths[connection] += 1
                else:
                    paths[connection] = 1
            continue
        elif connection == END:
            break
        else:
            paths, count = get_out(connection, end, steps=steps[:], paths=paths.copy(), current_path=current_path, return_counter=True)
            counter += count
    
    paths[start] = counter
    current_path.append(start)
    
    if return_counter:
        return paths.copy(), counter
    return paths.copy()

if __name__ == '__main__':
    steps = []
    for step in STEPS:
        paths = get_out(START, step, current_path=[])
        steps.append(paths[START])
    
    reverse = steps[0] > steps[1]

    true_path = [START]
    if reverse:
        for step in reversed(STEPS):
            true_path.append(step)
    else:
        for step in STEPS:
            true_path.append(step)
    true_path.append(END)

    counter = 1
    for i in range(len(true_path)-1):
        paths = get_out(true_path[i], true_path[i+1], current_path=[])
        counter *= paths[true_path[i]]
    
    print(counter)
