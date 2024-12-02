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

    for i, dist in enumerate(left_list):
        diff = left_list[i] - right_list[i]
        total += abs(diff)

    return total

print(get_distance(left_list, right_list))


