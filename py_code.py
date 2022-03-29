# code by Donal
# march 28, 2022
# to calculate the first term, common difference, sum of first 20 terms of an AP given a4 and a6

import numpy as np

# input parameter
a4 = 8
a6 = 14
n = 20

# output
d = (a6 - a4)/2
a1 = a4 - 3*d
s = n/2 * (2 * a1 + (n-1) * d)
print(d)
print(a1)
print(s)
