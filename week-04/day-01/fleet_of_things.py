from fleet import Fleet
from thing import Thing

#You have the Thing class
#You have the Fleet class
#You have the fleet_of_things.py file
#Download those, use those

fleet1 = Fleet()
thing1 = Thing("Get milk")
fleet1.add(thing1)
thing1 = Thing("Remove the obstacles")
fleet1.add(thing1)
thing1 = Thing("Stand up")
thing1.complete()
fleet1.add(thing1)
thing1 = Thing("Eat lunch")
thing1.complete()
fleet1.add(thing1)

print(fleet1)