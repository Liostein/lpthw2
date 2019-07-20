# a list allow you use number to get items out of list.
# but in dicts u can use anything as a index, almost
# u can use del to delete things in dicts

#creating a mapping of state to abbr
states = {
    'Oregon' : 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#creat a basic set of states and some cities in them
cities =  {
"CA" : "San Francisco",
"MI" : "Detroit",
"FL" : "Jacksonville"
}

#add some more cities
cities['NY'] = "New York"
cities['OR'] = "Portland"

#print out some cities
print '-' * 10
print "NY state has:", cities['NY']
print "OR state has:", cities['OR']

#print some states
print'-' * 10
print "Michigan's abbrev is:", states['Michigan']
print "Florida's abbrev is:", states['Florida']

# do it bt using the state then cities dict
print '-' * 10
print "Michigan has:", cities [states['Michigan']]
print "Florida has:", cities [states['Florida']]

#print every state abbrev
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbevitated %s" % (state, abbrev)

#print every city in state
print '-' * 10
for abbrev , city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# how do both at the same time ? use index
print '-'* 10
for state, abbrev in  states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
#safely get an abbrev by state that might not be there
state = states.get ('Texas',None)

if not state:
    print "Sorry, no Texas."
#get a city with a defult value

city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
