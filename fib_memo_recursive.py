'''
This is a recursive version of a fibonacci series
calculator
it returns the Nth term
It exploits memoisation making it more efficient
by not having to recalculate terms but lookin them up
'''

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
       return n
    else:
       memo[n] = (fib(n-1,memo) + fib(n-2,memo))
       return memo[n]

print(fib(60))