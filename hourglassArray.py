#!/bin/python3

'''
Objective:

Print the largest (maximum) hourglass sum found in Array A


Sample Input:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0



Sample Output:

19




Explaination:


An hourglass is represented like:

a b c
  d
e f g

Array A has the following hourglasses

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0


The hour glass with the maximum sum (19) is:

2 4 4
  2
1 2 4

'''

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)


def hourglassSum(pos):
    x, y = pos[0], pos[1]
    return arr[x-1][y-1] + arr[x-1][y] + arr[x-1][y+1] + arr[x][y] + arr[x+1][y-1] + arr[x+1][y] + arr[x+1][y+1]

centers = [
    [1,1],[1,2],[1,3],[1,4],
    [2,1],[2,2],[2,3],[2,4],
    [3,1],[3,2],[3,3],[3,4],
    [4,1],[4,2],[4,3],[4,4]
]

print(max(map(hourglassSum, centers)))
