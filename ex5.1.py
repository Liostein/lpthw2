name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "That is", height * 2.54, "centimeters."
print "He's %d pounds heavy." % weight
print "That is", weight * 0.45, "kg."
print "Actually that is not too heavy."
print "He is got %s eyes and %s hairs."% (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is trcky, try to get it exactly right
print "If I add %d ,%d, and %d I get %d." % (
    age, weight, height, age + weight + height)
