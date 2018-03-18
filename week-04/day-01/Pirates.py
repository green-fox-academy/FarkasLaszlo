class Pirate():
    def __init__(self,intoxication = 0, death = 0):
        self.intoxication = intoxication
        self.death = death

    def drink_some_rum(self):
        if self.death == 0:
            self.intoxication += 1
            return self.intoxication
        else:
            print('He\'s dead')

    def how_it_going_mate(self):
        if self.death == 0:
            if 4 >= self.intoxication >= 0:
                print('Pour me anudder')
            else:
                print('Arghh, I\'ma Pirate. How d\'ya d\'ink its goin?')
        else:
            print('He\'s dead')

    def die(self):
        self.death = 1

pirate1 = Pirate()
pirate1.how_it_going_mate()
pirate1.drink_some_rum()
pirate1.how_it_going_mate()
pirate1.drink_some_rum()
pirate1.how_it_going_mate()
pirate1.drink_some_rum()
pirate1.die()
pirate1.how_it_going_mate()
pirate1.drink_some_rum()
pirate1.how_it_going_mate()
pirate1.drink_some_rum()
pirate1.how_it_going_mate()
pirate1.drink_some_rum()
pirate1.how_it_going_mate()