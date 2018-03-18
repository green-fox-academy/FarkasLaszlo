import random

def draw_random_map():
    fw = open('map2.txt', 'w')
    for i in range(11):
        for x in range(10):
            a = random.randint(1, 4)
            if x == 0 and i == 0:
                fw.write('0')
            elif a == 1 or a == 2:
                fw.write('0')
            else:
                fw.write(str(random.randint(0, 1)))
        fw.write('\n')
    fw.close()

draw_random_map()
