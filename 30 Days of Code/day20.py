#Bubble Sort - Runtime of O(n^2)

#!/bin/python3

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

numSwaps = 0

a = list(map(int, a))
    
for j in range(1, n):
    for i in range(1, n):
        if a[i] < a[i-1]:
            a[i], a[i-1] = a[i-1], a[i]
            numSwaps += 1
        


print("Array is sorted in " + str(numSwaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[-1]))

