#import fuction from module
from sys import argv
#give the variable
script, filename = argv
# open file as txt
txt = open(filename)
# print filename and content
print "Here is your file %r:" % filename
print txt.read()
# ask for input filename again
print "Type the filename again:"
file_again = raw_input(">")
#open file as txt_again
txt_again = open(file_again)
# print its content
print txt_again.read()
txt.close()
txt_again.close()
