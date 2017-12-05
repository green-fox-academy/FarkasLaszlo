# Create a method that decrypts reversed-lines.txt
def decrypt(file_name):
    fw = open(file_name, 'r')
    code = open('good_lines.txt', 'w')
    text = fw.readlines()
    text_list = list(text)
    lineend = "\n"
    for x in range(len(text_list)):
        text_list[x] = text_list[x][::-1]
        text_list[x] = text_list[x].replace("\n","")+lineend
        code.write("".join(text_list[x]))

    fw.close()
    code.close()

decrypt("reversed-lines.txt")

code = open("good_lines.txt","r")
text = code.readlines()
for i in range(len(text)):
    print(text[i],sep="",end="")