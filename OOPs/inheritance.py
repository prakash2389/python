
########## Inheritance in Object-Oriented Programming (OOP)


# Class Definition
class calculator:
    # Method Definition
    def add(self,a,b):
        return a+b

    def subtract(self, a,b):
        return a-b

# Object Instantiation
cal = calculator()

# Invocation
cal.add(4,7)

# Inheritance
class modify_cal(calculator):
    def divide(self, a,b):
        return a/b

cal1 = modify_cal()

cal1.divide(2,5)

class new_modify_cal(modify_cal):
    def multiply(self, a,b):
        return a *b

cal2 = new_modify_cal()

cal2.multiply(2, 5)

