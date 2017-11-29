# Create a function called 'create_new_verbs()' which takes a list of verbs and a string as parameters
# The string shouldf be a preverb
# The function appends every verb to the preverb and returns the list of the new verbs


verbs = ["megy", "ver", "kapcsol", "rak", "néz"]
preverb = "be"

def create_new_verbs():
    newlist = []
    for i in verbs:
        newlist.append(preverb + i)

    return newlist

print(create_new_verbs())