"""Inheritance example showing method override with super()."""

class Vehicle:

    def start(self):
        print("Vehicle is starting.........")

    def stop(self):
        print("vehicle is stooping")

class Car(Vehicle):

    def check_fuel(self):
        print("Checking fuel...")

    def start(self):
        # Reuse parent behavior, then run child-specific logic.
        super().start()
        self.check_fuel()


# Demo run for parent and child objects.
p = Car()
r = Vehicle()

p.start()
r.stop()

r.start()
