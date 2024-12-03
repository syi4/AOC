with open('two_input.txt', 'r') as content:
    lines = content.readlines()
    data = [list(map(int, line.split())) for line in lines]

def get_safe(input):
    safe = 0

    for level in input:
        is_asc = all(level[i] <= level[i+1] and 1 <= (level[i+1] - level[i]) <= 3 for i in range(len(level) - 1))
        is_desc = all(level[i] >= level[i + 1] and 1 <= (level[i] - level[i + 1]) <= 3 for i in range(len(level) - 1))

        if is_asc or is_desc:
            safe += 1

    return safe

print(get_safe(data))



        