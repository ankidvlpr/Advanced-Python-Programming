"""Practice file focusing on __repr__ with composed objects."""

class Address:

    def __init__(self, street, city):
        self.street = street
        self.city = city
    
    def __repr__(self):
        # Detailed representation helpful during debugging.
        return f"(street={self.street}, city={self.city})"
    

class Person:                                          #Person has-a address
    def __init__(self, name, address):
        # super().__init__(street, city)

        self.name = name
        self.address = address
        

    def __repr__(self):
        # Nested repr keeps object details visible.
        return f"Person(name={self.name}, address={repr(self.address)})"
    
    


# Shared address object used by two Person instances.
add = Address("kalapathar", "ghaziabad")

p1 = Person("ANkit", add)
p2 = Person("Singh", add)

# print(p1)
# print(p2)
