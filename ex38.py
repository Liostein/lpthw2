ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split()
more_stuff = ["Day", "Night", "Song", "Frisbee","Corn","Banana","Girl", "Boy"]

while len(stuff)!= 10:
    next_one = more_stuff.pop()
    print "Adding:",next
    stuff.append(next_one)
    print "There is %d items now." % len (stuff)

print "There we go:"    ,stuff

print "Let us do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff) # what is this mean ? this means join space between every two items
print '#'.join(stuff[3:5])# add a # between element 3 and 4  , be careful this is not ordinal
