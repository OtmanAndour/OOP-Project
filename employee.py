# Python Object Oriented Programming


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_str(cls, emp_str):
        "An alternative constructor for string values"
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp_1 = Employee("Otman", "Andour", 50000)
emp_2 = Employee("Test", "User", 60000)

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"

new_emp_1 = Employee.from_str(emp_str_1)
print(new_emp_1.full_name())
