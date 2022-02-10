"""
A positive integer m can be expresseed as the sum of three squares if it is of the form p + q + r where p, q, r ≥ 0, and p, q, r are all perfect squares.
For instance, 2 can be written as 0+1+1 but 7 cannot be expressed as the sum of three squares. The first numbers that cannot be expressed as the sum of 
three squares are 7, 15, 23, 28, 31, 39, 47, 55, 60, 63, 71, … (see Legendre's three-square theorem).

Write a Python function threesquares(m) that takes an integer m as input and returns True if m can be expressed as the sum of three squares and False 
otherwise. (If m is not positive, your function should return False.)
"""
def threesquares(n):
  list1 = []
  flag = False
  for i in range(0, 100):
    for j in range(0,100):
      tempVar = (4^i)*((8*j)+7)
      list1.append(tempVar)
  if n not in list1 and n>0:
    flag = True
  else:
    flag = False
  return(flag)

"""
Write a function repfree(s) that takes as input a string s and checks whether any character appears more than once. The function should return True 
if there are no repetitions and False otherwise.
"""
def repfree(s):
  list1 = []
  flag = True
  for i in range(0, len(s)):
    if s[i] in list1:
      flag = False
    else:
      list1.append(s[i])
      flag = True
  return(flag)

"""
A list of numbers is said to be a hill if it consists of an ascending sequence followed by a descending sequence, where each of the sequences is of 
length at least two. Similarly, a list of numbers is said to be a valley if it consists of an descending sequence followed by an ascending sequence.
You can assume that consecutive numbers in the input sequence are always different from each other.

Write a Python function hillvalley(l) that takes a list l of integers and returns True if it is a hill or a valley, and False otherwise.
"""
def hillvalley(seq):
    is_dec, is_inc = False, False
    inflections = 0
    for i in range(len(seq)-1):
        if inflections > 1:
            # Early stop if more than 1 inflection
            return False
        right = seq[i+1]
        middle = seq[i]
        diff = right - middle
        if diff > 0:
            if is_dec:
                inflections += 1
            is_inc = True
            is_dec = False
        elif diff < 0:
            if is_inc:
                inflections += 1
            is_dec = True
            is_inc = False
    if inflections == 1:
        return True
    return False

