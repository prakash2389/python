

# Function Definition and Docstrings
#
# Function Deletion
#
# Function Wrapping / Decorators
#
# Execution Timing using a Decorator

# Decorators are a powerful feature in Python that allows you to modify or enhance the behavior of functions or methods.
# They are often used for logging, access control, memoization, and other cross-cutting concerns.
# Decorators are defined using the `@decorator_name` syntax and are applied to functions or methods.
# Function Definition


# Function with Docstring
def area_of_square(l, b):
    """
    Calculate the area of a square.
    :param l: #Length of the square
    :param b: #Breadth of the square
    :return:
    """
    return l * b

print(area_of_square(l = 19, b = 7))

# DOCSTRING
print(area_of_square.__doc__)

# Deleting a Function
del area_of_square


# Timing Wrapper Function
# A decorator is a special type of function that can modify or enhance the behavior of another function.
def time_wrapper(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")
        return result
    return wrapper

# Using the Wrapper Explicitly
s = time_wrapper(area_of_square)

s(2,6)

# Using the Wrapper as a Decorator
@time_wrapper
def area_of_square(l, b):
    """
    Calculate the area of a square.
    :param l: #Length of the square
    :param b: #Breadth of the square
    :return:
    """
    return l * b

area_of_square(4, 7)
