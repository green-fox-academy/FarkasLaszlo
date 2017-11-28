# - Create a function called `printer`
#   which prints the input parameters
#   (can have multiple number of arguments)

def printer(*argv):
    for arg in argv:
        print(arg)
a = 100
printer(a,"b",2.5,"d")
