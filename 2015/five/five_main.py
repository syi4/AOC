with open('five_input.txt', 'r') as content:
    data = content.read().strip().split("\n")

def is_nice(line):
    vowels = set("aeiou")
    vowel_count = sum(1 for char in line if char in vowels)

    has_double = any(line[i] == line[i + 1] for i in range(len(line) - 1))

    forbidden_substrings = ["ab", "cd", "pq", "xy"]
    has_forbidden = any(sub in line for sub in forbidden_substrings)

    return vowel_count > 2 and has_double and not has_forbidden

def get_nice(input):
    nice_count = sum(1 for line in input if is_nice(line))
    return nice_count

print(get_nice(data))


