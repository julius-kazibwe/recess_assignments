class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def increment_salary(self, increment_amount):
        self._salary += increment_amount

employee = Employee("Julius Kazibwe", 850000)
print("Employee:", employee.get_name())
print("Current Salary:", employee.get_salary())

# Increment the salary
increment_amount = 150000
employee.increment_salary(increment_amount)

print("New Salary:", employee.get_salary())
