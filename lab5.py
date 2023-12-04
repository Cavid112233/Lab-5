import math

def f(x):
    return x**2 - math.cos(x)

def df(x):
    return 2*x + math.sin(x)

def newton_raphson(initial_guess, epsilon, max_iterations):
    x = initial_guess
    iteration = 0

    while abs(f(x)) > epsilon and iteration < max_iterations:
        x = x - f(x) / df(x)
        iteration += 1

    return x

initial_guess = 0.5
epsilon = 1e-2
max_iterations = 1000

result = newton_raphson(initial_guess, epsilon, max_iterations)
print("təxmini nəticə:", result)
