### Lonely Integer ###

# Given an array of integers, where all elements but one occur twice, find the unique element.

# Example
# a = [1,2,3,4,3,2,1]
# The unique element is 4.

# Function Description
# Complete the lonelyinteger function in the editor below.
# lonelyinteger has the following parameter(s):
# ・int a[n]: an array of integers

# Returns
# int: the element that occurs only once

# Input Format
# The first line contains an single integer, n, the size of the array.
# The second line contains n space-separated integers that describe the values in a.

# Constraints
# ・1<=n<100
# ・It is guaranteed that n is an odd number and that there is one unique element.
# ・0<=a[i]<=100, where 0<=i<n

import math
import os
import random
import re
import sys

def lonelyinteger(a):
    res = 0
    for elem in a :
        res ^= elem #res will be reset if res encounters same number again  ^= XOR(排他的論理和)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()

#########################################

### Diagonal Difference ###

# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# For example, the square matrix arr is shown below:
# 1 2 3
# 4 5 6
# 9 8 9
# The left-to-right diagonal = 1+5+9=15. The right to left diagonal = 3+5+9=17. Their absolute difference is 15-17 = |2|.

# Function description
# Complete the diagonalDifference function in the editor below.
# diagonalDifference has the following parameter(s):
# ・int arr[n][n]: an array of integers

# Return
# ・int: the absolute difference

# Input Format
# The first line contains a single integer n, the number of rows and columns in the square matrix arr.
# Each of the next n lines describes a row, arr[i], and consists of n space-separated integers arr[i][j].

# Constraints
# ・-100 <= arr[i][j] <=100

# Output Format
# Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

# Sample Input
# 3
# 11 2 4
# 4 5 6
# 10 8 -12

# Sample Output
# 15

import math
import os
import random
import re
import sys

# sample input arr = [[11,2,4],[4,5,6],[10,8,-12]]

def diagonalDifference(arr):
    d1 = sum([arr[x][x] for x in range(len(arr))]) # range: give index(0,1,2) to x in arr
    d2 = sum([arr[x][n-1-x] for x in range(len(arr))])
    return (abs(d1-d2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

#########################################

### Counting Sort 1 ####

# Comparison Sorting
# Quicksort usually has a running time of n x log(n), but is there an algorithm that can sort even faster? In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. A comparison sort algorithm cannot beat n x log(n) (worst-case) running time, since n x log(n) represents the minimum number of comparisons needed to know where to place each element. For more details, you can see these notes (PDF).

# Alternative Sorting
# Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose index range covers the entire range of values in your array to sort. Each time a value occurs in the original array, you increment the counter at that index. At the end, run through your counting array, printing the value of each non-zero valued index that number of times.

# Example
# arr = [1,1,3,2,1]
# All of the values are in the range [0...3] , so create an array of zeros,result = [0,0,0,0] . The results of each iteration follow:
# i	arr[i]	result
# 0	1	[0, 1, 0, 0]
# 1	1	[0, 2, 0, 0]
# 2	3	[0, 2, 0, 1]
# 3	2	[0, 2, 1, 1]
# 4	1	[0, 3, 1, 1]
# The frequency array is [0,3,1,1]. These values can be used to create the sorted array as well: sorted = [1,1,1,2,3].

# Note
# For this exercise, always return a frequency array with 100 elements. The example above shows only the first 4 elements, the remainder being zeros.

# Challenge
# Given a list of integers, count and return the number of times each value appears as an array of integers.

# Function Description
# Complete the countingSort function in the editor below.
# countingSort has the following parameter(s):
# ・arr[n]: an array of integers

# Returns
# ・int[100]: a frequency array

# Input Format
# The first line contains an integer n, the number of items in arr.
# Each of the next n lines contains an integer arr[i] where 0<=i < n.

# Constraints
# 100 <= n <= 10^6
# 0 <= arr[i] < 100

# Sample Input
# 100
# 63 25 73 1 98 73 56 84 86 57 16 83 8 25 81 56 9 53 98 67 99 12 83 89 80 91 39 86 76 85 74 39 25 90 59 10 94 32 44 3 89 30 27 79 46 96 27 32 18 21 92 69 81 40 40 34 68 78 24 87 42 69 23 41 78 22 6 90 99 89 50 30 20 1 43 3 70 95 33 46 44 9 69 48 33 60 65 16 82 67 61 32 21 79 75 75 13 87 70 33

# Sample Output
# 0 2 0 2 0 0 1 0 1 2 1 0 1 1 0 0 2 0 1 0 1 2 1 1 1 3 0 2 0 0 2 0 3 3 1 0 0 0 0 2 2 1 1 1 2 0 2 0 1 0 1 0 0 1 0 0 2 1 0 1 1 1 0 1 0 1 0 2 1 3 2 0 0 2 1 2 1 0 2 2 1 2 1 2 1 1 2 2 0 3 2 1 1 0 1 1 1 0 2 2

import math
import os
import random
import re
import sys


def countingSort(arr):
    output = [0]*(max(arr)+1)

    for el in arr:
        output[el] += 1

    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

#########################################

#### Mock Test ####
### Flipping the Matrix ### (Level; Medium)

# Sean invented a game involving a 2nx2n matrix where each cell of the matrix contains an integer. He can reverse any of its rows or columns any number of times. The goal of the game is to maximize the sum of the elements in the nxn submatrix located in the upper-left quadrant of the matrix.
# Given the initial configurations for q matrices, help Sean reverse the rows and columns of each matrix in the best possible way so that the sum of the elements in the matrix's upper-left quadrant is maximal.

# Example
# matrix = [[1,2],[3,4]]

# 1 2
# 3 4

# It is 2x2 and we want to maximize the top left quadrant, a 1x1 matrix. Reverse row 1:
# 1 2
# 4 3

# And now reverse column 0:
# 4 2
# 1 3
# The maximal sum is 4.

# Function Description
# Complete the flippingMatrix function in the editor below.
# flippingMatrix has the following parameters:
# - int matrix[2n][2n]: a 2-dimensional array of integers

# Returns
# - int: the maximum sum possible.

# Input Format
# The first line contains an integer q, the number of queries.
# The next q sets of lines are in the following format:
# ・The first line of each query contains an integer, n.
# ・Each of the next 2n lines contains 2n space-separated integers matrix[i][j] in row i of the matrix.

# Constraints
# ・1 <= q <= 16
# ・1 <= n <= 128
# ・0 <= matrix[i][j] <= 4096, where 0 <= i, j < 2n

# Sample Input
# STDIN           Function
# -----           --------
# 1               q = 1
# 2               n = 2
# 112 42 83 119   matrix = [[112, 42, 83, 119], [56, 125, 56, 49], \
# 56 125 56 49              [15, 78, 101, 43], [62, 98, 114, 108]]
# 15 78 101 43
# 62 98 114 108

# Sample Output
# 414

# Explanation
# Start out with the following 2n x 2n matrix:

# matrix = [[112, 42, 83, 119],
#                [56, 125, 56, 49],
#                [15 78 101 43],
#                [62 98 114 108]]
# Perform the follwing operations to maximum the sum of the n x n submatrix in the upper-left quadrant:
# 2. Reverse column 2 ([83,56,101,114] -> [114,101,56,83]), resulting in the matrix:
# matrix = [[112,42 ,114,119],
#                [56,125,101,49],
#                [15,78,56,43],
#               [62,98,83,108]]
# 3. Reverse row 0 ([112,42,114,119] -> [119,114,42,112]), resulting in the matrix:
# matrix = [[119,114,42,112],
#                [56,125,101,49],
#                [15,78,56,43],
#                [62,98,83,108]]
# The sum of values in the n x n submatrix in the upper-left quadrant is 119+114+56+125 = 414.

q = int(input())
for _ in range(q):
    n = int(input())
    a = []
    for y in range(2*n):
        a.append([int(x) for x in input().split()])
    suma = 0
    for i in range(n):
        for j in range(n):
            suma += max(max(a[i][j],a[2*n-i-1][j]),max(a[i][2*n-j-1],a[2*n-i-1][2*n-j-1]))
    print(suma)
























