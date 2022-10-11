# The pattern is fairly easy to see. 
# The output in the ith index of the array is the product of all
# input elements expect the element in the ith index in the input array.

import numpy as np

#converting the input elements seperated by spaces to a list and then to an array
a = np.array([int(item) for item in input("Enter the list items : ").split()])

#empty output array
n = np.empty(len(a))

#non zero array from a; np.nonzero returns the indices of all non zero elements
b = np.nonzero(a)

#product of all non zero elements of a
p = np.prod(b)

zeroes = len(a)-len(b)
#creating the output array element by element
for i in range(len(a)):
    #no zero elements case
    if zeroes == 0:
        n[i] = p//a[i]

    # multiple zeroes mean that output is a zero array    
    elif zeroes > 1:
        n[i] = 0

    # single zero case, avoiding nesting
    elif zeroes == 1 and a[i] != 0:
        n[i] = 0
    else: n[i] = p
print(n)
