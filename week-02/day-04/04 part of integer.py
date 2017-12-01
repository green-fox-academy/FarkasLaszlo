input_list = [19, 2, 3, 25, 21, 19, 32, 31, 41, 65, 45167, 161, 710, 18, 18312, 818]
number = 1

def part(input_list, number):
    out = []
    for i in range(len(input_list)):
        n = 0
        for x in range(len(str(input_list[i]))):
            if int((input_list[i] / (10**x)) % 10) == number:
                if n == 0:
                    out.append(i)
                    n += 1
    return out

print(part(input_list, number))