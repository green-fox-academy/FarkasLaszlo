from tkinter import *
import random
#from draw_random_map import draw_random_map

root = Tk()
canvas = Canvas(root, width=792, height=792)

floor = PhotoImage(file="floor.png")
wall = PhotoImage(file="wall.png")


def read_file():
    file = open("map.txt", "r")
    line = file.readlines()
    file.close()
    return line


class Character:
    def __init__(self, d6):
        self.d6 = d6
        self.d6 = random.randint(1, 6)


class Monsters:
    def __init__(self, monster_type, d6):
        self.d6 = d6
        self.canvas = canvas
        self.monster_type = monster_type
        self.skeleton = PhotoImage(file="skeleton.png")
        self.boss = PhotoImage(file="boss.png")
        self.x = 0
        self.y = 0
        line = read_file()
        self.coord_list = []
        i = 0
        if self.monster_type == "Skeleton":
            self.hp = 2 * self.d6
            self.dp = 1 / 2 * self.d6
            self.sp = self.d6
            self.max_hp = 2 * self.d6
        elif self.monster_type == "Boss":
            self.hp = 3 * self.d6
            self.dp = self.d6
            self.sp = self.d6
            self.max_hp = 2 * self.d6
        while i < 4:
            self.x = random.randint(0, 720)//72
            self.y = random.randint(0, 792)//72
            if [self.x, self.y] not in self.coord_list and line[self.y][self.x] == "0" and self.x + self.y != 0:
                self.coord_list.append([self.x, self.y])
                i += 1
        print(self.coord_list)

    def draw_skeleton(self):
        for i in range(len(self.coord_list)-1):
            x = self.coord_list[i][0]
            y = self.coord_list[i][1]
            self.canvas.create_image(x*72 + 36, y*72 + 36, image=self.skeleton)

    def draw_boss(self):
        if len(self.coord_list) > 0:
            x = self.coord_list[len(self.coord_list)-1][0]
            y = self.coord_list[len(self.coord_list)-1][1]
            self.canvas.create_image(x * 72 + 36, y * 72 + 36, image=self.boss)


class Hero(Character):
    def __init__(self, d6):
        super().__init__(d6)
        self.canvas = canvas
        self.hp = 20 + 3 * self.d6
        self.max_hp = 20 + 3 * self.d6
        self.dp = 2 * self.d6
        self.sp = 5 + self.d6
        self.hero_down = PhotoImage(file="hero-down.png")
        self.hero_up = PhotoImage(file="hero-up.png")
        self.hero_left = PhotoImage(file="hero-left.png")
        self.hero_right = PhotoImage(file="hero-right.png")
        self.herox = 36
        self.heroy = 36

    def draw_down(self):
        self.canvas.create_image(self.herox, self.heroy, image=self.hero_down)

    def draw_up(self):
        self.canvas.create_image(self.herox, self.heroy, image=self.hero_up)

    def draw_left(self):
        self.canvas.create_image(self.herox, self.heroy, image=self.hero_left)

    def draw_right(self):
        self.canvas.create_image(self.herox, self.heroy, image=self.hero_right)


def draw_map(floor, wall):
    line = read_file()
    for i in range(len(line)):
        for x in range(len(line[i])):
            if line[i][x] == "0":
                canvas.create_image(x*72+36, 72*i+36, image=floor)
            elif line[i][x] == "1":
                canvas.create_image(x*72+36, 72*i+36, image=wall)


draw_map(floor, wall)
hero1 = Hero(0)
hero1.draw_right()
monsters1 = Monsters("Skeleton", hero1.d6)
monsters1.draw_skeleton()
monsters1.draw_boss()
print(monsters1.d6, hero1.d6)


def on_key_press(e):
    line = read_file()
    if e.keycode == 38:
        if hero1.heroy > 36 and line[hero1.heroy//72 - 1][hero1.herox//72] == "0":
            hero1.heroy = hero1.heroy - 72
        draw_map(floor, wall)
        hero1.draw_up()
        monsters1.draw_skeleton()
        monsters1.draw_boss()
    elif e.keycode == 40:
        if hero1.heroy < (len(line)-1) * 72 + 36 and line[hero1.heroy//72 + 1][hero1.herox//72] == "0":
            hero1.heroy = hero1.heroy + 72
        draw_map(floor, wall)
        hero1.draw_down()
        monsters1.draw_skeleton()
        monsters1.draw_boss()
    elif e.keycode == 37:
        if hero1.herox > 36 and line[hero1.heroy//72][hero1.herox//72 - 1] == "0":
            hero1.herox = hero1.herox - 72
        draw_map(floor, wall)
        hero1.draw_left()
        monsters1.draw_skeleton()
        monsters1.draw_boss()
    elif e.keycode == 39:
        if hero1.herox < len(line) * 72 - 36 and line[hero1.heroy//72][hero1.herox//72 + 1] == "0":
            hero1.herox = hero1.herox + 72
        draw_map(floor, wall)
        hero1.draw_right()
        monsters1.draw_skeleton()
        monsters1.draw_boss()
    if [hero1.herox//72, hero1.heroy//72] in monsters1.coord_list:
        fight(hero1.herox//72, hero1.heroy//72)
        print(monsters1.coord_list)


def fight(x, y):
    try:
        for i in range(len(monsters1.coord_list)):
            if [x, y] == monsters1.coord_list[i]:
                monsters1.coord_list.pop(i)
        while hero1.hp > 0 and monsters1.hp > 0:
            if monsters1.d6 * 2 + monsters1.sp > hero1.dp:
                hero1.hp = hero1.hp - monsters1.sp
            if hero1.d6 * 2 + hero1.sp > monsters1.dp:
                monsters1.hp = monsters1.hp - hero1.sp
            if hero1.hp <= 0:
                print("hero lost")
        if len(monsters1.coord_list) == 0:
            print("hero won")

    except IndexError:
        pass


canvas.bind("<KeyPress>", on_key_press)
canvas.pack()
canvas.focus_set()
root.mainloop()
