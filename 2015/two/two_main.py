with open('two_input.txt', 'r') as content:
    data = content.read().strip().split('\n')

def get_wrapping_paper(input):
    total = 0

    for str in input:
        s = str.split('x')
        l = int(s[0])
        w = int(s[1])
        h = int(s[2])

        total += (2 * l * w) + (2 * w * h) + (2 * h * l) + min(l * w, w * h, h * l)

    return total

def get_ribbon(input):
    total = 0

    for str in input:
        s = str.split('x')
        l = int(s[0])
        w = int(s[1])
        h = int(s[2])

        nums = [l, w, h]
        sorted_nums = sorted(nums)

        smallest = sorted_nums[0]
        second_smallest = sorted_nums[1]

        total += 2 * (smallest + second_smallest) + (l * w * h)

    return total


print(get_ribbon(data))
