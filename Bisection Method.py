def function(t):
    return t**3-25.0


error = 10**(-6)
no_of_iterations = 0


def recursion(a, b, no_of_iterations):
    x_n = (a+b)/2
    if abs(function(x_n)) <= error:
        print(f'The approximate root is {x_n} and the number of iterations is {no_of_iterations}')
    elif function(x_n) * function(a) < 0:
        no_of_iterations += 1
        recursion(a, x_n, no_of_iterations)
    elif function(x_n) * function(b) < 0:
        no_of_iterations += 1
        recursion(x_n, b, no_of_iterations)


recursion(2, 3, no_of_iterations)
