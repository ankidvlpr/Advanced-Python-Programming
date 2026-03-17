"""Company roster example using custom string formatting."""

class Person:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
class Company:

    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, person):
        # Store employee entry in company list.
        self.employees.append(person)

    def __str__(self):
        # Build multiline summary of company + employee names.
        result = f"{self.name} ({len(self.employees)} employees)"

        for employee in self.employees:
            result += f"\n- {employee}"

        return result

        

company = Company("OpenAi")

company.add_employee("singh")
company.add_employee("Rahul")
company.add_employee("Rahul")
company.add_employee("Rahul")

# Demo: print full company roster.
print(company)

        

        
