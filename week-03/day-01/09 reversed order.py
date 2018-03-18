# Create a method that decrypts reversed-order.txt
def decrypt(file_name):
    fw = open(file_name, 'r')
    code = open('good_order.txt', 'w')
    text = fw.readlines()
    text = text[::-1]
    text_list = list(text)
    lineend = '\n'
    for x in range(len(text_list)):
        text_list[x] = text_list[x].replace('\n', '') + lineend
        code.write(''.join(text_list[x]))


    fw.close()
    code.close()

decrypt('reversed-order.txt')

code = open('good_order.txt', 'r')
text = code.readlines()
for i in range(len(text)):
    print(text[i], sep='', end='')