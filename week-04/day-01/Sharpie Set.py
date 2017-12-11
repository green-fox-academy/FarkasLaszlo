#Reuse your Sharpie class
#Create SharpieSet class
#it contains a list of Sharpie
#count_usable() -> sharpie is usable if it has ink in it
#remove_trash() -> removes all unusable sharpies
from sharpie import Sharpie

object1 = Sharpie("blue", 3.5, 0)
object2 = Sharpie("green", 1.5, 50)
object3 = Sharpie("red", 1, 100)
object4 = Sharpie("yellow", 2.5, 20)

lista = [object1, object2, object3, object4]
for i in range(len(lista)):
    print(lista[i].color,lista[i].width,lista[i].ink_amount)


class SharpieSet():

    def count_usable(self):
        count = 0
        for i in range(len(lista)):
            if lista[i].ink_amount > 0:
                count +=1
        print(count)

    def remove_trash(self):
        no_trash_list = []
        for i in range(len(lista)):
            if lista[i].ink_amount > 0:
                no_trash_list.append(lista[i])
        return no_trash_list


SharpieSet.count_usable(lista)
lista = SharpieSet.remove_trash(lista)

for i in range(len(lista)):
    print(lista[i].color,lista[i].width,lista[i].ink_amount)