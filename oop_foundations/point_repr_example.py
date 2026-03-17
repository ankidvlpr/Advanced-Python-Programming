"""Small practice for custom __repr__ output."""

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # Developer-friendly string representation of Point object.
        return f"Point(x={self.x}, y={self.y})"
    
# Demo: calling repr() explicitly.
point = Point(1,2)
print(repr(point))  
