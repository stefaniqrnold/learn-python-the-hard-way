## Animal is-a object (this is a base class, so it's a bit of a special case)
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object (this is a base class, so it's a bit of a special case)
class Person(object):
    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet
        self.pet = None

## Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        ## Calls the __init__ method of the Person class
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object (this is a base class, so it's a bit of a special case)
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet, satan is-a pet
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet, rover is-a pet
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
