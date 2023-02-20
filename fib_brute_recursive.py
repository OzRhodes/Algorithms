'''
This is a recursive version of a fibonacci series
calculator
it returns the Nth term
It is brute force and so recalculates many of the fib(n) calcs 
making it very inefficient
'''

def fib(n):
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))

print(fib(40))