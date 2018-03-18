# Write a program that opens a file called 'my-file.txt', then prints
# each of lines form the file.
# If the program is unable to read the file (for example it does not exists),
# then it should print an error message like: 'Unable to read file: my-file.txt'
try:
    fw = open('my-file.txt', 'r')
    text = fw.readlines()
    for i in range(len(text)):
        print(text[i], sep='', end='')
except:
    print('Unable to read file: my-file.txt')

fw.close()