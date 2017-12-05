# Create a method that find the 5 most common lottery numbers otos.csv
def five_most_frequent(file_name):
    fw = open(file_name,"r")
    text = fw.readlines()
    big_number_list = list()
    number_list = list()
    frequent_list = [0]*90
    frequent_dict = ""
    for i in range(len(text)):
        big_number_list = text[i].split("t")[4].strip()
        big_number_list = big_number_list.split(";")
        del(big_number_list[0])
        number_list.append(big_number_list)

    for i in range(len(number_list)):
        for x in range(5):
            frequent_list[int(number_list[i][x]) - 1] += 1

    frequent_dict = dict(zip(range(1,91),frequent_list))
    frequent_dict = sorted(frequent_dict.items(), reverse=True, key=lambda t: t[1])
    number_list = list()
    for i in range(5):
        number_list.append(frequent_dict[i][0])
    return number_list

print(five_most_frequent("otos.csv"))