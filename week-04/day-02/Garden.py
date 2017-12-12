class Garden():
    def __init__(self, garden):
        self.garden = garden

    def add_tree(self, tree):
        self.garden.append(tree)

    def add_flower(self, flower):
        self.garden.append(flower)

    def watering(self, number):
        count = 0
        for i in range(len(self.garden)):
            if self.garden[i].type == "Flower" and self.garden[i].water_level < 5:
                count += 1
            elif self.garden[i].type == "Tree" and self.garden[i].water_level < 10:
                count += 1
        if count == 0:
            print("Nothing needs water")
            return
        print("Watering with "+str(number))
        number /= count
        for i in range(len(self.garden)):
            if self.garden[i].type == "Flower" and self.garden[i].water_level < 5:
                self.garden[i].water_level += number * 0.75
                if self.garden[i].water_level < 5:
                    print("The "+str(self.garden[i].name)+" "+str(self.garden[i].type)+" needs water")
                else:
                    print("The "+str(self.garden[i].name)+" "+str(self.garden[i].type)+" doesn't need water")
            elif self.garden[i].type == "Tree" and self.garden[i].water_level < 10:
                self.garden[i].water_level += number * 0.4
                if self.garden[i].water_level < 10:
                    print("The "+str(self.garden[i].name)+" "+str(self.garden[i].type)+" needs water")
                else:
                    print("The "+str(self.garden[i].name)+" "+str(self.garden[i].type)+" doesn't need water")
            else:
                print("The "+str(self.garden[i].name)+" "+str(self.garden[i].type)+" doesn't need water")


class Flower():
    def __init__(self, name, type="Flower", water_level=0):
        self.water_level = water_level
        self.name = name
        self.type = type


class Tree():
    def __init__(self, name, type="Tree", water_level=0):
        self.water_level = water_level
        self.name = name
        self.type = type


tree1 = Tree("purple")
tree2 = Tree("orange")
tree3 = Tree("red")
flower1 = Flower("yellow")
flower2 = Flower("blue")
flower3 = Flower("green")

garden1 = Garden([])
garden1.add_flower(flower1)
garden1.add_flower(flower2)
garden1.add_flower(flower3)
garden1.add_tree(tree1)
garden1.add_tree(tree2)
garden1.watering(0)
garden1.watering(40)
garden1.watering(70)
