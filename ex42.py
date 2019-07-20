## Animals is a object look at the extra credit
class Animal (object):
    pass

## dog is an Animal
class dog(Animal):

    def __init__(self, name):
        ## self has a attribute name and set is name
        self.name = name

## cat is an animal
class Cat(Animal):
    def __init__ (self, name):
        ## cat has a name
        self.name = name


## person is a object
class Person (object):

    def __ init__ (self, name):
        ##  Person has a name
        self.name = name

        ## Person has a pet of some kind
        self.pet = None

## Employee is a object
class Employee (Person):

    def __init__ (self, name, salary):
        ## person has a name ,
        super(Employee,self). __init__ (name)
        ##  person has a salary
        self.salary = salary

## fish is a class
class Fish (object):
    pass

## Salmon is a fish
class Salmon (Fish):
    pass

##  Halibut is a fish
class Halibut (Fish):
    pass


## rover is a dog
rover = Dog ("Rover")

## satan is a cat
satan = Cat("Satan")

## mary is a person
mary = Person ("Mary")

## mary has a pet called satan
mary.pet = satan

## frank is a employee 120000
frank = Employee("Frank",120000)

## frank has a pet rover
frank.pet = rover

## flipper is a fish
flipper = Fish ()

##crouse is a Salmon
crouse = Salom()

 ##
 harry = Halibbut()
