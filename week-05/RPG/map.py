from tkinter import *
from draw_random_map import *

root = Tk()
canvas = Canvas(root, width=720, height=792)

floor = PhotoImage(file="floor.png")
wall = PhotoImage(file="wall.png")


def read_file():
    file = open("map.txt", "r")
    line = file.readlines()
    file.close()
    return line


class Monsters:
    def __init__(self, monster_type, canvas, max_hp=0, hp=0, dp=0, sp=0, ):
        self.canvas = canvas
        self.hp = hp
        self.dp = dp
        self.sp = sp
        self.max_hp = max_hp
        self.monster_type = monster_type
        self.skeleton = PhotoImage(file="skeleton.png")
        self.boss = PhotoImage(file="boss.png")
        self.x = 0
        self.y = 0
        line = read_file()
        self.coord_list = []
        i = 0
        while i < 4:
            self.x = random.randint(0, 720)//72
            self.y = random.randint(0, 792)//72
            if [self.x, self.y] not in self.coord_list and line[self.y][self.x] == "0" and self.x + self.y != 0:
                self.coord_list.append([self.x, self.y])
                i += 1

    def draw_monsters(self):
        for i in range(len(self.coord_list)):
            x = self.coord_list[i][0]
            y = self.coord_list[i][1]
            if i < len(self.coord_list)-1:
                self.canvas.create_image(x*72 + 36, y*72 + 36, image=self.skeleton)
            else:
                self.canvas.create_image(x * 72 + 36, y * 72 + 36, image=self.boss)


class Hero:
    def __init__(self, canvas, max_hp=0, hp=0, dp=0, sp=0):
        self.canvas = canvas
        self.hp = hp
        self.max_hp = max_hp
        self.dp = dp
        self.sp = sp
        self.hero_down = PhotoImage(file="hero-down.png")
        self.hero_up = PhotoImage(file="hero-up.png")
        self.hero_left = PhotoImage(file="hero-left.png")
        self.hero_right = PhotoImage(file="hero-right.png")
        self.herox = 36
        self.heroy = 36
        self.hp = 20

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


draw_random_map()
draw_map(floor, wall)
hero1 = Hero(canvas)
hero1.draw_right()
monsters1 = Monsters("Skeleton", canvas)
monsters1.draw_monsters()


def on_key_press(e):
    line = read_file()
    if e.keycode == 38 and hero1.heroy > 36 and line[hero1.heroy//72 - 1][hero1.herox//72] == "0":
        draw_map(floor, wall)
        hero1.heroy = hero1.heroy - 72
        hero1.draw_up()
        monsters1.draw_monsters()
    elif e.keycode == 40 and hero1.heroy < 756 and line[hero1.heroy//72 + 1][hero1.herox//72] == "0":
        draw_map(floor, wall)
        hero1.heroy = hero1.heroy + 72
        hero1.draw_down()
        monsters1.draw_monsters()
    elif e.keycode == 37 and hero1.herox > 36 and line[hero1.heroy//72][hero1.herox//72 - 1] == "0":
        draw_map(floor, wall)
        hero1.herox = hero1.herox - 72
        hero1.draw_left()
        monsters1.draw_monsters()
    elif e.keycode == 39 and hero1.herox < 684 and line[hero1.heroy//72][hero1.herox//72 + 1] == "0":
        draw_map(floor, wall)
        hero1.herox = hero1.herox + 72
        hero1.draw_right()
        monsters1.draw_monsters()


canvas.bind("<KeyPress>", on_key_press)
canvas.pack()
canvas.focus_set()
root.mainloop()
