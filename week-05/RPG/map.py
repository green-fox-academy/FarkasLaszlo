from tkinter import *
import random

root = Tk()
canvas = Canvas(root, width=720, height=792)

floor = PhotoImage(file="floor.png")
wall = PhotoImage(file="wall.png")


def read_file():
    file = open("map.txt", "r")
    line = file.readlines()
    file.close()
    return line


class Character:
    def __init__(self, hp, dp, sp):
        self.hp = hp
        self.dp = dp
        self.sp = sp
        self.d6 = random.randint(1, 6)


class Monsters(Character):
    def __init__(self, hp, dp, sp, monster_type):
        super().__init__(hp, dp, sp)
        self.monster_type = monster_type
        if monster_type == "Skeleton":
            self.hp = 2 * self.d6
            self.dp = 0.5 * self.d6
            self.sp = self.d6
        elif monster_type == "Boss":
            self.hp = 3 * self.d6
            self.dp = self.d6
            self.sp = self.d6
        self.skeleton = PhotoImage(file="skeleton.png")
        self.boss = PhotoImage(file="skeleton.png")

    def draw_skeletons(self):
        line = read_file()
        counter = 0
        x = random.randint(72, 720)//72
        y = random.randint(72, 792)//72
        monster_list = []
        while counter < 3:
            if line[x][y] == "0":
                pass


class Hero(Character):
    def __init__(self, canvas, hp=0, dp=0, sp=0):
        super().__init__(hp, dp, sp)
        self.canvas = canvas
        self.hero_down = PhotoImage(file="hero-down.png")
        self.hero_up = PhotoImage(file="hero-up.png")
        self.hero_left = PhotoImage(file="hero-left.png")
        self.hero_right = PhotoImage(file="hero-right.png")
        self.herox = 36
        self.heroy = 36
        self.hp = 20 + 3 * self.d6
        self.dp = 2 * self.d6
        self.sp = self.d6

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
hero1 = Hero(canvas)
hero1.draw_right()


def on_key_press(e):
    line = read_file()
    if e.keycode == 38 and hero1.heroy > 36 and line[hero1.heroy//72 - 1][hero1.herox//72] == "0":
        draw_map(floor, wall)
        hero1.heroy = hero1.heroy - 72
        hero1.draw_up()
    elif e.keycode == 40 and hero1.heroy < 756 and line[hero1.heroy//72 + 1][hero1.herox//72] == "0":
        draw_map(floor, wall)
        hero1.heroy = hero1.heroy + 72
        hero1.draw_down()
    elif e.keycode == 37 and hero1.herox > 36 and line[hero1.heroy//72][hero1.herox//72 - 1] == "0":
        draw_map(floor, wall)
        hero1.herox = hero1.herox - 72
        hero1.draw_left()
    elif e.keycode == 39 and hero1.herox < 684 and line[hero1.heroy//72][hero1.herox//72 + 1] == "0":
        draw_map(floor, wall)
        hero1.herox = hero1.herox + 72
        hero1.draw_right()


canvas.bind("<KeyPress>", on_key_press)
canvas.pack()
canvas.focus_set()
root.mainloop()
