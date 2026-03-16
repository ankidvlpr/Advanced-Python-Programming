"""Simple counter class practice with basic state updates."""

class Counter:

    def __init__(self, start=0):
        self.start = start
        self.current = start

    def inc(self):
        self.current += 1
        return self.current

    def add(self, n):
        self.current += n
        return self.current
    
    def reset(self):
        # Bring the counter back to the original starting point.
        self.current = self.start 
        return self.current
       
    def value(self):
        return self.current
    
    
# Quick usage demo of the class methods.
p = Counter()
print(p.inc())
print(p.add(2))
print(p.value())
print(p.reset())
