

########## Generator #########

# concept of generators in Python
# A generator is a special type of iterator that allows you to iterate over a sequence of values without storing them all in memory at once.
# Generators are defined using functions with the `yield` keyword or by using generator expressions.
# Generators are more memory efficient than lists, especially when dealing with large datasets.
# Generators are iterators, but not all iterators are generators.

# Basic Generator Function
def gen_numbers(n):
    for chunk in range(n):
        yield chunk

chunk = gen_numbers(10)

for i in chunk:
    print(i)


# Generator Expression
gen = (i+5 for i in [1, 6, 4, 8, 4] if i<5)

for i in gen:
    print(i)


# List vs Generator in Performance and Memory

a = [i for i in range(1000000000)]

t1 = time.time()
sum(a)
t2 = time.time()
print(t2-t1)

b = (i for i in range(1000000000))
t1 = time.time()
sum(b)
t2 = time.time()
print(t2-t1)

# Use generators when you're working with large datasets or streams of data (e.g., log files, sensor data)