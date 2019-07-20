from sys import argv

script, input_file = argv

def print_all(f):
    print  f.read()
#f.seek() seek by bytes,0 means to the start position
def rewind(f):
    f.seek(0)
#f.readline() read a line after another eachtime it's called
def print_a_line(line_count, f)  :
    print line_count, f.readline()
    #add a ,(comma) at the end of print so readline doesn't print its own \n
    #for example: print line_count, f,readline(),

current_file = open(input_file)

print "First let's print the whole file: \n"

print_all(current_file)

print "Now let's rewind,kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1

print_a_line(current_line, current_file)
#also it could be +=
current_line +=  1
print_a_line(current_line,current_file)
