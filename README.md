## Bisection-Method
This is the python implenentation of the bisection method with the following:
1) f(x)= x^3-25  // This function can be edited easily from the function definition included under the function
2) Error between the actual root of the function and the approximate root is set to be 10^(-6)
3) For the above function, the interval choosen is [2,3] by the manual computations using Intermediate value theorem and calculus.

#Outputs:
1) It prints the approximate root of the function. Here, it is 2.9240177273750305
2) It also prints the actual number of iterations taken to produce the approximate root. Here, 24 number of iterations are required.


# Warning:
The program uses recursive method instead of iterative method. Therefore, care should be taken if the number of theoritical iterations exceeds more than 1000. The system limit needs to be adjusted and integrate the following code:

import sys

sys.setrecursionlimit(100000)
