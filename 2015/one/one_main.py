with open('one_input.txt', 'r') as content:
    data = content.read()

def count_floor(input):
    return input.count('(') - input.count(')')

def find_basement(input):
    upper = 0
    lower = 0

    for i, dir in enumerate(input):
        if lower > upper:
            print(f"UP: {upper}")
            print(f"DOWN: {lower}")
            return i
        
        if dir == '(':
            upper += 1
        else:
            lower += 1


    return None

print(find_basement(data))


