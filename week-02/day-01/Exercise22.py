a = 24
out = 0
# if w is even increment out by one
w = input('w= ')
if a == int(w):
    out += 1
print(out)




b = input('b= ')
out2 = ''
# if b is between 10 and 20 set out2 to "Sweet!"
# if less than 10 set out2 to "More!",
# if more than 20 set out2 to "Less!"
b = int(b)
if 10 < b < 20:
    out2 = 'Sweet!'
elif b < 10:
    out2 = 'More!'
else:
    out2 = 'Less!'

print(out2)



c = 123
credits = 100
is_bonus = False
# if credits are at least 50,
# and is_bonus is false decrement c by 2
# if credits are smaller than 50,
# and is_bonus is false decrement c by 1
# if is_bonus is true c should remain the same
if credits >= 50 and is_bonus == False:
    c -= 2
elif credits < 50 and is_bonus == False:
    c -= 1
elif is_bonus == True:
    c = c

print(c)




d = 7
time = 150
out3 = ''
# if d is dividable by 4
# and time is not more than 200
# set out3 to "check"
# if time is more than 200
# set out3 to "Time out"
# otherwise set out3 to "Run Forest Run!"
if not d % 4 and time <= 200:
    out3 = 'check'
elif time > 200:
    out3 = 'Time out'
else:out3 = 'Run Forest Run!'

print(out3)
