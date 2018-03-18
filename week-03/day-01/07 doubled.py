# Create a method that decrypts the duplicated-chars.txt

def decrypt(file_name):
    fw = open(file_name, 'r')
    code = open('simple_chars.txt', 'w')
    text = fw.readlines()
    text_list = list(text)
    for x in range(len(text_list)):
        text_list[x] = text_list[x][::2]
    code.write(''.join(text_list))

    fw.close()
    code.close()

decrypt('duplicated-chars.txt')

code = open('simple_chars.txt','r')
text = code.readlines()
for i in range(len(text)):
    print(text[i], sep='', end='')
