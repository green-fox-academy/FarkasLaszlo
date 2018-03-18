# Create a method that decrypts encoded-lines.txt
def decrypt(file_name):
    fw = open(file_name, 'r')
    code = open("decoded_lines.txt", 'w')
    text = fw.readlines()
    text_list = list(text)
    number = 0
    for x in range(len(text_list)):
        element = list(text_list[x])
        for i in range(len(text_list[x])):
            if not element[i] == ' ' and not element[i] == '\n':
                number = ord(element[i])
                number -= 1
                element[i] = chr(number)

        code.write(''.join(element))

    fw.close()
    code.close()

decrypt("encoded-lines.txt")

code = open("decoded_lines.txt", 'r')
text = code.readlines()
for i in range(len(text)):
    print(text[i],sep = '',end='')