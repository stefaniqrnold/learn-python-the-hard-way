class Other(object):
    def override(self):
        print("OTHER override()")
    
    def implicit(self):
        print("OTHER implicit()")
        
    def altered(self):
        print("OTHER altered()")
        
class Child(object):
    def __init__(self):
        self.other = Other()  # Composition: Child has an instance of Other
        
    def implicit(self):
        self.other.implicit()  # Delegating to the Other instance
        
    def override(self):
        print("CHILD override()")  # Overriding the behavior
    
    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()  # Delegating to the Other instance
        print("CHILD, AFTER OTHER altered()")
        
son = Child()

son.implicit()  # Delegates to Other.implicit()
son.override()  # Child's own method
son.altered()   # Delegates to Other.altered() with additional behavior in Child