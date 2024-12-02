with open('three_input.txt', 'r') as content:
    data = content.read()

def get_unique_houses(input):
    current = (0, 0)
    house_set = {current}

    moves = {
        '^': (0, 1),  
        'v': (0, -1),  
        '<': (-1, 0),  
        '>': (1, 0)    
    }

    for dir in input:
        dx, dy = moves[dir]
        current = (current[0] + dx, current[1] + dy)
        house_set.add(current)

    return len(house_set)

print(get_unique_houses(data))



