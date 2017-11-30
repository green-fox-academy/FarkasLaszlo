input_list = [1, 2, 21, 21, 1, 31, 31, 4, 55, 55, 6, 7, 8, 88, 88]


def unique_list(input_list):

    out = []
    for i in input_list:
        if i not in out:
            out.append(i)
    return out

print(unique_list(input_list))
