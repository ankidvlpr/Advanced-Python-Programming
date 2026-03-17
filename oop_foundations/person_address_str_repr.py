"""Practice file for __str__ and __repr__ with has-a relationship."""

class Address:

    def __init__(self, street, city):
        self.street = street
        self.city = city
    
    def __str__(self):
        # Human-readable address format.
        return f"{self.street}, {self.city}"
    
    def __repr__(self):
        return f"(street={self.street}, city={self.city})"
    

class Person:                                          #Person has-a address
    def __init__(self, name, address):

        self.name = name
        self.address = address

    def __str__(self):
        # End-user friendly print output.
        return f"{self.name} - {self.address}"
     

    def __repr__(self):
        return f"Person(name={self.name}, address={repr(self.address)})"
    

add = Address("kalapathar", "ghaziabad")

p1 = Person("ANkit", add)
p2 = Person("Singh", add)

# Demo output for string conversion methods.
print(add)
print(p1)

# print(p1)
# print(p2)
