with open('one_input.txt', 'r') as content:
    left_list = []
    right_list = []
    
    for line in content:
        parts = line.strip().split()

        left_list.append(int(parts[0]))
        right_list.append(int(parts[1]))

    left_list.sort()
    right_list.sort()

def get_distance(left_list, right_list):
    total = 0

    for i, _ in enumerate(left_list):
        diff = left_list[i] - right_list[i]
        total += abs(diff)

    return total

def get_similarity(left_list, right_list):
    total = 0

    for i, _ in enumerate(left_list):
        count = right_list.count(left_list[i])
        total += count * left_list[i]

    return total

print(get_similarity(left_list, right_list))


