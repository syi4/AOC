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

def get_unique_by_santa_and_robo(input):
    santa_current = (0, 0)
    robo_current = (0, 0)
    house_set = {santa_current}

    moves = {
        '^': (0, 1),  
        'v': (0, -1),  
        '<': (-1, 0),  
        '>': (1, 0)    
    }

    for i, dir in enumerate(input):
        dx, dy = moves[dir]
        
        if i % 2 == 0:
            santa_current = (santa_current[0] + dx, santa_current[1] + dy)
            house_set.add(santa_current)
        else:
            robo_current = (robo_current[0] + dx, robo_current[1] + dy)
            house_set.add(robo_current)
    
    return len(house_set)

print(get_unique_by_santa_and_robo(data))



