with open('four_input.txt', 'r') as content:
    data = content.read().strip().split('\n')

def is_bound(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

def get_word(input):
    ans = 0

    rows = len(input)
    cols = len(input[0])

    directions = [
       ([-1, 0], [-2, 0], [-3, 0]),  # North
        ([1, 0], [2, 0], [3, 0]),     # South
        ([0, 1], [0, 2], [0, 3]),     # East
        ([0, -1], [0, -2], [0, -3]),  # West
        ([-1, 1], [-2, 2], [-3, 3]),  # North-East
        ([-1, -1], [-2, -2], [-3, -3]),  # North-West
        ([1, 1], [2, 2], [3, 3]),     # South-East
        ([1, -1], [2, -2], [3, -3])   # South-West
    ]

    def found(dir):
        return (
            input[dir[0][0]][dir[0][1]] == 'M' and
            input[dir[1][0]][dir[1][1]] == 'A' and
            input[dir[2][0]][dir[2][1]] == 'S'
        )

    def search(r, c):
        total = 0
        for direction in directions:
            new_positions = [[r + d[0], c + d[1]] for d in direction]
          
            if all(is_bound(pos[0], pos[1], rows, cols) for pos in new_positions):
                if found(new_positions):
                    total += 1

        return total

    for r in range(rows):
        for c in range(cols):
            if input[r][c] == 'X':
                ans += search(r, c)

    return ans

def get_count(input):
    ans = 0

    rows = len(input)
    cols = len(input[0])

    directions = [
       ([-1, -1], [1, 1]),  
        ([-1, 1], [1, -1]),
    ]

    def found(dir):
        return(
            input[dir[0][0]][dir[0][1]] == 'M' and
            input[dir[1][0]][dir[1][1]] == 'S' or
            input[dir[0][0]][dir[0][1]] == 'S' and
            input[dir[1][0]][dir[1][1]] == 'M'
        )

    def is_x(r, c):
        for direction in directions:
            new_positions = [[r + d[0], c + d[1]] for d in direction]

            if all(is_bound(pos[0], pos[1], rows, cols) for pos in new_positions):
              
                 if found(new_positions):
                    return True
        return False

    for r in range(rows):
        for c in range(cols):
            if input[r][c] == 'A' and is_x(r, c):
                ans += 1
                
    return ans


print(get_count(data))

