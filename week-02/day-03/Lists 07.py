# Accidentally I messed up this quote from Richard Feynman.
# Two words are out of place
# Your task is to fix it by swapping the right words with code

# Also, print the sentence to the output with spaces in between.

words = ["What", "I", "do", "create,", "I", "cannot", "not", "understand."]
i, j = words.index("cannot"), words.index("do")
words[i], words[j] = words[j], words[i]
print(words[0]+" "+words[1]+" "+words[2]+" "+words[3]+" "+words[4]+" "+words[5]+" "+words[6]+" "+words[7])