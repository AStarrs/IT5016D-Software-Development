
class Employee:

    num_of_emps = 0
    raise_ammount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_ammount)
        # self.pay = int(self.pay * Employee.raise_ammount) - class variables should
        # be accessed through the class (Employee) or the instace (self).

emp_1 = Employee('Anna', 'Starovoytova', 70000)
emp_2 = Employee('Anton', 'Starovoytov', 100000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
'''emp_1 argument passes automatically in the empty parentasies, thats why it's
important to use self argument when creating methods'''

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.__dict__)

Employee.raise_ammount = 1.05

print(Employee.raise_ammount)
print(emp_1.raise_ammount)
print(emp_2.raise_ammount)

''''change variable for only one instance '''
emp_1.raise_ammount = 1.05

print(emp_1.__dict__)