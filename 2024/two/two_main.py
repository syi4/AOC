with open('two_input.txt', 'r') as content:
    lines = content.readlines()
    data = [list(map(int, line.split())) for line in lines]

def is_safe(level):
    is_asc = all(level[i] <= level[i+1] and 1 <= (level[i+1] - level[i]) <= 3 for i in range(len(level) - 1))
    is_desc = all(level[i] >= level[i + 1] and 1 <= (level[i] - level[i + 1]) <= 3 for i in range(len(level) - 1))

    return is_asc or is_desc

def get_safe_two(input):
    safe = 0

    for level in input:
        if is_safe(level):
            safe += 1
        else:
            for i in range(len(level)):
                new_level = level[:i] + level[i + 1:]

                if is_safe(new_level):
                    safe += 1
                    break

    return safe


print(get_safe_two(data))



        