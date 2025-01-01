with open('five_input.txt', 'r') as content:
    p1, p2 = content.read().strip().split("\n\n")
    
    pages = []
    for line in p1.split('\n'):
        a, b = line.split("|")
        pages.append((int(a), int(b)))

    updates = [list(map(int, line.split(','))) for line in p2.split('\n')]

def get_answer(update):
    idx = {}
    for i, num in enumerate(update):
        idx[num] = i

    for a, b in pages:
        if a in idx and b in idx and not idx[a] < idx[b]:
            return False, 0
        
    return True, update[len(update) // 2]

ans = 0

for update in updates:
    good, mid = get_answer(update)
    if good:
        ans += mid

print(ans)