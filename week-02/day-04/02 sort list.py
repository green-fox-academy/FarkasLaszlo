input_list = [1, 2, 25, 21, 1, 31, 31, 4, 65, 55, 6, 7, 8, 98, 88]
reverse = False

def sort_list(input_list, reverse):
        out = sorted(input_list, reverse = reverse)
        return out


print(sort_list(input_list,reverse))