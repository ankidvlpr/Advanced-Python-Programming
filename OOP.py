"""
OOP practice (based on the list in your screenshot).

1) Basic class and object
2) Instance methods and `self`
3) Inheritance
4) Encapsulation (private attribute)
6) Class variables
7) Static method
8) Property decorators
9) Inheritance + `isinstance()`
10) Multiple inheritance
"""


class Car:
    """A simple `Car` class used to demonstrate core OOP concepts."""

    # 6) Class variable: shared across all instances.
    total_car = 0

    def __init__(self, brand: str, model: str):
        """
        Create a new car.

        4) Encapsulation:
        - `__brand` and `__model` use name-mangling, so they are "private-ish"
          (can't be accessed as `obj.__brand` from outside the class).
        """
        self.__brand = str(brand).strip()
        self.__model = str(model).strip()

        # Increment the shared counter whenever a new Car (or subclass) is created.
        Car.total_car += 1

    def get_brand(self) -> str:
        """
        Getter method (topic #4 style).

        For topic #8 we also expose `brand` using `@property`.
        """
        return self.__brand + "!"

    # 8) Property decorators (getter + setter)
    @property
    def brand(self) -> str:
        """Brand of the car (read/write) using a property."""
        return self.__brand

    @brand.setter
    def brand(self, value: str) -> None:
        value = str(value).strip()
        if not value:
            raise ValueError("brand cannot be empty")
        self.__brand = value

    # 8) Property decorators (read-only example)
    @property
    def model(self) -> str:
        """Model of the car (read-only)."""
        return self.__model

    def full_name(self) -> str:
        """Return a readable full name for the car."""
        return f"{self.__brand} {self.__model}"

    def fuel_type(self) -> str:
        """
        Default implementation.

        3) Inheritance: subclasses can override this to change behavior.
        """
        return "Petrol or Diesel"

    # 7) Static method
    @staticmethod
    def general_description() -> str:
        """
        Static method: does not depend on `self` (instance) or `cls` (class).

        It's just a utility function grouped under the class namespace.
        """
        return "Car are means of transport"


class ElectricCar(Car):
    """A `Car` subclass that adds battery information and changes fuel type."""

    def __init__(self, brand: str, model: str, battery_size: str):
        # Call the parent constructor to reuse initialization logic.
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self) -> str:
        """Override: electric cars don't use petrol/diesel."""
        return "Electric Charge"


class Battery:
    """Feature class used for multiple inheritance (topic #10)."""

    def battery_info(self) -> str:
        return "this is battery"


class Engine:
    """Another feature class used for multiple inheritance (topic #10)."""

    def engine_info(self) -> str:
        return "this is engine"


class ElectricCarTwo(Battery, Engine, Car):
    """
    10) Multiple inheritance.

    This class gets methods from multiple parents:
    - `battery_info()` from `Battery`
    - `engine_info()` from `Engine`
    - `full_name()`, `fuel_type()`, etc. from `Car`

    Note: Because `Battery` and `Engine` don't define `__init__`, Python will
    eventually call `Car.__init__` via the MRO when we create `ElectricCarTwo`.
    """


def main() -> None:
    """Runs small demos for topics #1–#10 when this file is executed."""
    # 1) Basic class + object (instances)
    my_tesla = ElectricCar("tesla", "S class", "89kwh")
    my_car = Car("Toyota", "coralla")

    # 3) Inheritance + overriding
    print(my_tesla.fuel_type())
    print(my_car.fuel_type())

    # 6) Class variable: counts how many cars were created
    print(Car.total_car)

    # 7) Static method call (no object needed)
    print(Car.general_description())

    # 8) Property decorators
    print(my_car.model)  # read-only property
    print(my_car.brand)  # read/write property
    my_car.brand = "Honda"
    print(my_car.full_name())

    # 9) Inheritance + isinstance()
    print(isinstance(my_tesla, Car))  # True: ElectricCar IS-A Car
    print(isinstance(my_car, ElectricCar))  # False: Car is not ElectricCar

    # 10) Multiple inheritance
    my_new_tesla = ElectricCarTwo("tesla", "model s")
    print(my_new_tesla.engine_info())
    print(my_new_tesla.battery_info())


if __name__ == "__main__":
    main()
