# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# The square should have as many lines as the number was
a = input("A number: ")
a = int(a)
a -=1
n = 1
b = "%"
c = " "
print((a+1)*b)
while n<a:
    print(b+(n-1)*c+b+(a-n-1)*c+b)
    n+=1
print((a+1)*b)