import numpy as np
# Array called "mixnums" composed of 3 integers and 3 floats. Then print.
mixnums = np.array([9, 4, 13, 17.5, 14.1, 21.2])
print(mixnums)
# Create an array called "mixtypes" composed of 2 integers, 2 floats, and 2 strings. Then print.
mixtypes = np.array([12, 6, 21.5, 12.7, 'circe', 'helios'])
print(mixtypes)
# Create an array called "oddarray" of all odd numbers between 0 and 100. Then print.
oddarray = np.arange(1,100,2)
print(oddarray)
# Create an array called "logarray" of 16 numbers between 1 and 5 that follow a logarithmic distribution. Then print.
logarray = np.logspace(1,5,16)
print(logarray)