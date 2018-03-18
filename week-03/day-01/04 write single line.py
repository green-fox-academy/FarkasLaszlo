# Open a file called 'my-file.txt'
# Write your name in it as a single line
# If the program is unable to write the file,
# then it should print an error message like: 'Unable to write file: my-file.txt'
try:
    fw = open('my-file2.txt', 'w')
    fw.write('Farkas László')
except FileNotFoundError:
    print('Unable to wrtie file: my-file.txt')

fw.close()

fw = open('my-file2.txt', 'r')
text = fw.readlines()
for i in range(len(text)):
    print(text[i],sep='',end='')

fw.close()