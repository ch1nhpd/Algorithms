# Python program to generate
# odd sized magic squares
# A function to generate odd
# sized magic squares
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    all_magic = [[8, 1, 6, 3, 5, 7, 4, 9, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4], [4, 3, 8, 9, 5, 1, 2, 7, 6],
             [2, 7, 6, 9, 5, 1, 4, 3, 8], [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 9, 2, 3, 5, 7, 8, 1, 6],
             [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 3, 4, 1, 5, 9, 6, 7, 2]]
    s_1d = []
    for ii in s:
        for i in ii:
            s_1d.append(i)

    min = 100
    for m in all_magic:
        diff = 0
        for i, j in zip(s_1d, m):
            diff += abs(j - i)
        if diff < min:
            min = diff 
    return min



def generateSquare(n):#bonus
    # 2-D array with all
    # slots set to 0
    magicSquare = [[0 for x in range(n)]
                   for y in range(n)]

    # initialize position of 1
    i = n / 2
    j = n - 1

    # Fill the magic square
    # by placing values
    num = 1
    while num <= (n * n):
        if i == -1 and j == n:  # 3rd condition
            j = n - 2
            i = 0
        else:

            # next number goes out of
            # right side of square
            if j == n:
                j = 0

            # next number goes
            # out of upper side
            if i < 0:
                i = n - 1

        if magicSquare[int(i)][int(j)]:  # 2nd condition
            j = j - 2
            i = i + 1
            continue
        else:
            magicSquare[int(i)][int(j)] = num
            num = num + 1

        j = j + 1
        i = i - 1  # 1st condition

    # Printing magic square
    print("Magic Square for n =", n)
    print("Sum of each row or column",
          n * (n * n + 1) / 2, "\n")

    for i in range(0, n):
        for j in range(0, n):
            print('%2d ' % (magicSquare[i][j]),
                  end='')

            # To display output
            # in matrix form
            if j == n - 1:
                print()


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     s = []
#
#     for _ in range(3):
#         s.append(list(map(int, input().rstrip().split())))
#
#     result = formingMagicSquare(s)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()



n = 3
generateSquare(n)

# This code is contributed
# by Harshit Agrawal
