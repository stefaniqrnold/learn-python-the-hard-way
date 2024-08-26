# Defines a class named Parent that inherits from the base class `object`.
class Parent(object): 
    # Defines a method named `override` in the Parent class. This method prints a specific message.
    def override(self): 
        print("PARENT override()") # This method is not overridden yet, but it will be in the Child class.
        
    # Defines a method named `implicit` in the Parent class. This method prints a specific message.
    def implicit(self): 
        print("PARENT implicit()") # This method is not overridden in the Child class.
        
    # Defines a method named `altered` in the Parent class. This method prints a specific message.
    def altered(self): 
        print("PARENT altered()") # This method will be overridden in the Child class.
        
# Defines a class named Child that inherits from the Parent class.
class Child(Parent): 
    # Defines a method named `override` in the Child class, overriding the one from the Parent class.
    def override(self): 
        print("CHILD override()") # This overrides the `override` method in the Parent class.
        
    # Defines a method named `altered` in the Child class, which first prints a message,
    # then calls the `altered` method from the Parent class using `super()`,
    # and finally prints another message.
    def altered(self): 
        print("CHILD, BEFORE PARENT altered()") # Custom behavior before calling the Parent's `altered`.
        super(Child, self).altered() # Calls the Parent's `altered` method.
        print("CHILD, AFTER PARENT altered()") # Custom behavior after calling the Parent's `altered`.
        
# Creates instances of the Parent and Child classes.
dad = Parent()
son = Child()

# Calls the `implicit` method on the Parent instance.
dad.implicit() # Expected output: "PARENT implicit()"

# Calls the `implicit` method on the Child instance.
son.implicit() # Expected output: "PARENT implicit()"
# The Child class does not override this method, so it uses the one from the Parent class.

# Calls the `override` method on the Parent instance.
dad.override() # Expected output: "PARENT override()"

# Calls the `override` method on the Child instance.
son.override() # Expected output: "CHILD override()"
# This method is overridden in the Child class.

# Calls the `altered` method on the Parent instance.
dad.altered() # Expected output: "PARENT altered()"

# Calls the `altered` method on the Child instance.
son.altered() 
# Expected output:
# "CHILD, BEFORE PARENT altered()"
# "PARENT altered()"
# "CHILD, AFTER PARENT altered()"
# This method is overridden in the Child class.
