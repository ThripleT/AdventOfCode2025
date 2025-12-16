CONNECTIONS = {}
for line in open('11-input.txt').read().splitlines():
    connection = line.split()
    CONNECTIONS[connection[0].removesuffix(':')] = connection[1:]

def get_out(start, end, counter=0):
    for connection in CONNECTIONS[start]:
        if connection == end:
            counter += 1
            break
        else:
            counter += get_out(connection, end)
        
    return counter

if __name__ == '__main__':
    print(get_out('you', 'out'))