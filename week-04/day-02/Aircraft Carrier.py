class Aircraft:
    def __init__(self, type, damage = 0, max_ammo = 0, ammo = 0):
        self.type = type
        self.ammo = ammo
        self.damage = damage
        self.max_ammo = max_ammo
        if self.type == 'F16':
            self.damage = 30
            self.max_ammo = 8
        elif self.type == 'F35':
            self.damage = 50
            self.max_ammo = 12

    def fight(self):
        damage = self.damage * self.ammo
        self.ammo = 0
        return damage

    def refill(self, number):
        if number > self.max_ammo:
            self.ammo = self.max_ammo
            return number - self.max_ammo

    def gettype(self):
        return self.type

    def getstatus(self):
        print('Type ' + self.type +', Ammo:' + str(self.ammo) + ' Base Damage: ' + str(self.damage)
              + ' All damage ' + str(self.damage*self.ammo))


class Carrier:
    def __init__(self, aircrafts, initial_ammo = 30, health_point = 5000):
        self.aircrafts = aircrafts
        self.initial_ammo = initial_ammo
        self.health_point = health_point

    def addAircraft(self, aircraft):
        self.aircrafts.append(aircraft)

    def fill(self):
        if self.initial_ammo == 0:
            print('The aircraft carrier has no ammunition')
            return
        f16 = 0
        f35 = 0
        for i in range(len(self.aircrafts)):
            if self.aircrafts[i].type == 'F16':
                f16 += 1
            elif self.aircrafts[i].type == 'F35':
                f35 += 1
        needed_ammo = f16 * 8 + f35 * 12
        if needed_ammo > self.initial_ammo:
            for i in range(len(self.aircrafts)):
                if self.aircrafts[i].type == 'F35' and self.initial_ammo >= self.aircrafts[i].max_ammo:
                    self.aircrafts[i].ammo = self.aircrafts[i].max_ammo
                    self.initial_ammo = self.initial_ammo - self.aircrafts[i].max_ammo
                elif self.aircrafts[i].type == 'F35' and 0 < self.initial_ammo < self.aircrafts[i].max_ammo:
                    self.aircrafts[i].ammo = self.initial_ammo
                    self.initial_ammo = 0
            if self.initial_ammo > 0:
                for i in range(len(self.aircrafts)):
                    if self.aircrafts[i].type == 'F16' and self.initial_ammo >= self.aircrafts[i].max_ammo:
                        self.aircrafts[i].ammo = self.aircrafts[i].max_ammo
                        self.initial_ammo = self.initial_ammo - self.aircrafts[i].max_ammo
                    elif self.aircrafts[i].type == 'F16' and 0 < self.initial_ammo < self.aircrafts[i].max_ammo:
                        self.aircrafts[i].ammo = self.initial_ammo
                        self.initial_ammo = 0
        else:
            for i in range(len(self.aircrafts)):
                self.aircrafts[i].ammo = self.aircrafts[i].max_ammo
                self.initial_ammo = self.initial_ammo - self.aircrafts[i].max_ammo

    def fight(self, carrier):
        damage = 0
        for i in range(len(self.aircrafts)):
            damage += self.aircrafts[i].damage * self.aircrafts[i].ammo
            self.aircrafts[i].ammo = 0
        carrier.health_point -= damage
        if carrier.health_point < 0 and self.health_point > 0:
            print('We won')
        elif carrier.health_point > 0 and self.health_point > 0:
            print('We haven\'t finished')
        elif self.health_point <= 0:
            print('We lost')

    def getstatus(self):
        total_damage = 0
        for i in range(len(self.aircrafts)):
            total_damage += self.aircrafts[i].ammo * self.aircrafts[i].damage
        if self.health_point == 0:
            print('It\'s dead Jim :(')
            return
        else:
            print('HP: ' + str(self.health_point) + ', Aircraft count: ' + str(len(self.aircrafts)) + ', Ammo Storage: '
            + str(self.initial_ammo) + ' Total Damage: ' + str(total_damage))
        print('Aircrafts:')
        for i in range(len(self.aircrafts)):
            print('Type ' + self.aircrafts[i].type + ', Ammo:' + str(self.aircrafts[i].ammo) + ' Base Damage: '
                  + str(self.aircrafts[i].damage)
                  + ' All damage ' + str(self.aircrafts[i].damage * self.aircrafts[i].ammo))


aircraft1 = Aircraft('F16')
aircraft2 = Aircraft('F16')
aircraft6 = Aircraft('F16')
aircraft3 = Aircraft('F35')
aircraft4 = Aircraft('F35')
aircraft5 = Aircraft('F35')
aircraft7 = Aircraft('F35')

carrier1 = Carrier([], 500, 1000)
carrier1.addAircraft(aircraft1)
carrier1.addAircraft(aircraft2)
carrier1.addAircraft(aircraft6)
carrier1.addAircraft(aircraft3)
carrier1.addAircraft(aircraft4)
carrier1.addAircraft(aircraft5)
carrier1.addAircraft(aircraft7)
carrier1.fill()
carrier1.getstatus()

carrier2 = Carrier([], 10, 5000)
carrier1.fight(carrier2)
carrier1.fill()
carrier1.getstatus()
carrier1.fight(carrier2)
carrier1.fight(carrier2)
