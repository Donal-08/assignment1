# code by Donal
# april 13, 2022
# to calculate the first term, common difference, sum of first 20 terms of an AP given a4 and a6

import numpy as np

# input parameters
n = 20
a_i = 8
a_j = 14
i = 4
j = 6


# Functions

def common_diff(i, j, a_i, a_j):
    """ This function takes inputs i,j,a_i,a_j and returns the  COMMON DIFFERENCE
         of the A.P whose a_i = i'th term and a_j = j'th term are given
    """
    d = (a_j - a_i) / (j - i)
    return d


def first_term(i, j, a_i, a_j):
    """ This function takes inputs i,j,a_i,a_j and computes the  FIRST TERM
        of the A.P whose a_i = i'th term and a_j = j'th term are given
    """
    d = (a_j - a_i) / (j - i)
    a_1 = a_i - (i - 1) * d
    return a_1


def Sum(n, i, j, a_i, a_j):
    """ This function takes inputs n,i,j,a_i,a_j and returns the " SUM OF n TERMS "
             of the A.P whose a_i = i'th term and a_j = j'th term are given
        """
    d = (a_j - a_i) / (j - i)
    a_1 = a_i - (i - 1) * d
    S_n = n / 2 * (2 * a_1 + (n - 1) * d)
    return S_n


# output to verify the correctness

_d = common_diff(i, j, a_i, a_j)
_a1 = first_term(i, j, a_i, a_j)
_Sn = Sum(n, i, j, a_i, a_j)

print(_d)
print(_a1)
print(_Sn)
