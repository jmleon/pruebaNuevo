#!/usr/bin/python
"""
Si alguien usando nuestro programa quiere obtener 13 numeros de la secuencia de fibonacci
deben editar el probrama a mano. 
If someone using our program wants to get 13 numbers in the Fibonacci sequence
(or 10 or 100 or any other number), they have to edit our program by hand.
That's a hassle, so Python has LIBRARIES (collections of tools) that allow you
to pass arguments to the program at RUNTIME (when you run the program).
"""
import sys # This library provides system-specific functions.
times = int( # Force the parameter to be an integer.
	sys.argv[1] # The first argument after the program name.
)
# Define a function (fib) which takes one parameter (t).
def fib(t):
	f = [ 0, 1 ]
	for i in range(len(f),t):
		fn = f[len(f)-1] + f[len(f)-2]
		f.append(fn)
	print f
	fib(times) # Call function fib and pass the value of times as its parameter.
"""
Result:
$ ~: fibonacci.py 12
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
$ ~: fibonacci.py 15
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
NOTE: If you use anything other than a number as an argument, the program will
crash when you try to run it. Can you find a way to make sure the argument is
a number?
"""
