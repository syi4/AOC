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

print(get_wrapping_paper(data))
