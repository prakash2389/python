def generate(x):
    fibonacci = [0,1]
    k = fibonacci[-1] + fibonacci[-2]
    while k<x:
        k= fibonacci[-1] + fibonacci[-2]
        fibonacci.append(k)
    return fibonacci

print(generate(200))


