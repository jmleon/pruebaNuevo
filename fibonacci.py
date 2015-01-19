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


