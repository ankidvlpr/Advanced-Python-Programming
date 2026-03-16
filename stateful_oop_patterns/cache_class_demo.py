"""Basic cache object for storing, reading, and clearing key-value data."""

class Cache:

    def __init__(self, initial=None):
        if initial is None:
            self.data = {}
        else:
            # Copy the incoming data so the cache has its own storage.
            self.data = dict(initial)

    def set(self,k,v):
        self.data[k] = v
    
    def get(self, k , default=None):

        if k in self.data:
            return self.data[k]
        else:
            default
        
    def clear(self):
        self.data = {}


# Simple cache usage example.
c1 = Cache()
c2= Cache()

c1.set("user","ankit")
print(c1.data)

print(c1.get("user"))

c1.clear()
print(c1.data)
