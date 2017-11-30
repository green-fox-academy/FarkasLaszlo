input_list = [ 1, 2, 3, 25, 21, 1, 32, 31, 41, 65, 45167, 161, 710, 18, 18312, 818]
number = 7

def part(input_list, number):
    out = []
    for i in range(len(input_list)):
        for x in range(len(str(input_list[i]))):
            if input_list[i] == number:
                out.append(i)
            elif input_list[i] % (10*(x+1)) == number:
                out.append(i)
            elif x > 0:
                if int((input_list[i] / (10**x)) % 10) == number:
                    out.append(i)

    out = sorted(set(out))
    return out
print(part(input_list,number))