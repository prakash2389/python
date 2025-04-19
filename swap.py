

###### Swapping two numbers without using a third variable

a = 20
b = 10

a = a + b
b = a - b
a = a - b

print(a, b)


a = 20
b = 10



a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)


a = input("Enter a: ")
b = input("Enter b: ")


a, b = b, a

print(a, b)
