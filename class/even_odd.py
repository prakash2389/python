import numbers

class EVENODD:
    def __init__(self):
        pass

    def check_if_odd_or_even(self, x):
        if x % 2 == 0:
            return "even"
        else:
            return "odd"



even_odd = EVENODD()
# from test import MyFunctions
# even_odd = MyFunctions()
number = "10.5"

if isinstance(number, numbers.Number):
  output  = even_odd.check_if_odd_or_even(number)
  print(f"The {number} is {output}")
else:
  print(f"Please enter a number but you entered {number}")
