
### Program to check if a number is even or odd and stop on "STOP" or after 10 inputs
### This program will take user input and check if the number is even or odd.


b=0
while True:
    a = input("Enter number:   ")
    if a == "STOP" or b==10:
        break
    try:
        a = int(a)
        if a%2==0:
            print("Even")
        else:
            print("Odd")
    except:
        print("Enter valid number")
    b = b+1
print("Task completed")
