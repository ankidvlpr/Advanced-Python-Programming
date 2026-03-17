"""Polymorphism example with a shared DataLoader interface."""

class DataLoader:
    def __init__(self, src):
        self.src = src

    def load(self):
        # Force subclasses to define their own loading behavior.
        raise NotImplementedError

    def __repr__(self):
        return f"{self.__class__.__name__}(src='{self.src}')"

class CSVLoader(DataLoader):
    def __init__(self, src):
        super().__init__(src)

    def load(self):
        # CSV-specific loading flow.
        print(f"Loading csv data from {self.src}")
        print("Parsing CSV file...")



class JSONLoader(DataLoader):
    def __init__(self, src):
        super().__init__(src)

    def load(self):
        # JSON-specific loading flow.
        print(f"Loading JSON data from {self.src}")
        print("Parsing JSon file...")


# Same interface (`load`) works for different loader types.
csv_loader = CSVLoader("Data.csv")
json_loader = JSONLoader("Data.json")


print(csv_loader)
print(json_loader)

csv_loader.load()
json_loader.load()

