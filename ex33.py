

# assign i a initial number 0
i = 0
# assign numbers a empty list
numbers = []

while i < 6 :
    print "At the top i is %d" % i

    numbers.append(i)
    i = i+1
    print "Numbers now:" ,numbers

    print "At the bottom i is %d" % i


print "The numnbers:"

for num in numbers:
    print num
