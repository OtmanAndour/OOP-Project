# Python Object Oriented Programming


import datetime


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

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

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {} ".format(self.full_name(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())


class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, list_emp=None):
        super().__init__(first, last, pay)
        if list_emp is None:
            self.list_emp = []
        self.list_emp = list_emp

    def add_emp(self, emp):
        if emp not in self.list_emp:
            self.list_emp.append(emp)

    def remove_emp(self, emp):
        if emp in self.list_emp:
            self.list_emp.remove(emp)

    def print_emp(self):
        for emp in self.list_emp:
            print(emp.full_name())


emp_1 = Employee("Otman", "Andour", 50000)
emp_2 = Employee("Test", "User", 60000)

# print(emp_1+emp_2)

#mg_1 = Manager('Jack', 'Daniel', 80000, [dev_1])

# print(emp_1.__repr__())
# print(emp_1.__str__())

emp_1.first = "Jim"

print(emp_1.first)
print(emp_1.email)
print(emp_1.full_name())
