# Create a function called 'reverse_string' which takes a string as a parameter
# The function reverses it and returns with the reversed string

reversed = '.eslaf eb t\'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI'

def reverse_string(reversed):
    reversed = reversed[::-1]
    return reversed
print(reverse_string(reversed))