# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

def copy(file1,file2):
    try:
        a = open(file1,"r")
        b = open(file2,"w")
        text = a.readlines()
        for i in range(len(text)):
            b.write(text[i])
        b.close()
        a.close()
        return True
    except:
        return False

print(copy("file to copy.txt", "copy to this.txt"))

