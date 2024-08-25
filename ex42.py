## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a animal
class Dog(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## Cas is-a animal
class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):
    def __init__(self, name):
        ## Person has-a name of some kind
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a person
class Employee(Person):
    def __init__(self, name, salary):
        ## calls the specific attributtes of father class
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet, satan is-a pet
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()
