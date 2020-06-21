# Python Object Oriented Programming


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def full_name(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee("Otman", "Andour", 50000)
emp_2 = Employee("Test", "User", 60000)

# print(emp_1)
# print(emp_2)

print(emp_1.full_name())
print(emp_2.full_name())

print(Employee.full_name(emp_1))
