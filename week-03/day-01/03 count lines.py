# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.
fw = open('sample.txt', 'w',)
fw.write("writing some stuff in my text file\nIt's a totally new line\nAnd another one")
fw.close()


def line_counter(name):
    try:
        fw = open(name, 'r')
        number = sum(1 for line in fw)
        fw.close()
        return number
    except FileNotFoundError:
        return 0


print(line_counter('sample.txt'))
print(line_counter("my-file.txt"))