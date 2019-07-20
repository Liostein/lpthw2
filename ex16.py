from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
print "If you don't want that,hit CTRL-C(^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename,'w')

print "Truncating the file. Goodbye! "
target.truncate()

print "Now I am going to ask for three lines."

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "I am going to write these to the file."
# bad linwa
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

#good lines
target.write(("%s\n%s\n%s\n") % (line1, line2, line3))

print "And finally, we close it."
target.close()
