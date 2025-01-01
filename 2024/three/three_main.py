import re

with open('three_input.txt', 'r') as content:
    data = content.read()

    def get_answer(input):
        do = True
        answer = 0
        i = 0

        while i < len(input):
            if input[i:i + 4] == "do()":
                do = True
                i += 4
            elif input[i:i + 7] == "don't()":
                do = False
                i += 7
            elif input[i:i+4] == 'mul(':
                i += 4

                first = 0

                while input[i].isdigit():
                    first = first * 10 + int(input[i])
                    i += 1

                if input[i] == ',':
                    i += 1

                second = 0

                while input[i].isdigit():
                    second = second * 10 + int(input[i])
                    i += 1

                if input[i] == ')':
                    if do:
                        answer += first * second
                    i += 1
            else:
                i += 1

        return answer
        

print(get_answer(data))
