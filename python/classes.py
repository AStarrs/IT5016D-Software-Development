
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)

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
