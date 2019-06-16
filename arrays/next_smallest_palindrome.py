'''
Given a number, in the form of an array a[] containing digits from 1 to 9(inclusive). 
The task is to find the next smallest palindrome larger than this number.
Input: n and followed by an array of digit of length n

11
9 4 1 8 7 9 7 8 3 2 2

Output:
9 4 1 8 8 0 8 8 1 4 9
'''

from heapq import heappush, heappop
min_heap = []
max_heap = []
N = int(input())
d1, d2 = int(input()), int(input())
print(d1)
if d1 <= d2:
    heappush(min_heap, d2)
    heappush(max_heap, -d1)
else:
    heappush(min_heap, d1)
    heappush(max_heap, -d2)
print(int((d1 + d2)/2))
for i in range(2,N):
    d = int(input())
    min_ = min_heap[0]
    if d > min_:
        heappush(min_heap, d)
    else:
        heappush(max_heap, -d)
    if len(min_heap) - len(max_heap) == 2:
        min_ = heappop(min_heap)
        heappush(max_heap, - min_)
    if len(max_heap) - len(min_heap) ==  2:
        max_ = - heappop(max_heap)
        heappush(min_heap, max_)    
    if len(min_heap) - len(max_heap) == 1:
        print(int(min_heap[0]))
    elif len(min_heap) - len(max_heap) == -1:
        print(int(-max_heap[0]))
    else:
        result = (min_heap[0] - max_heap[0])*0.5
        print(int(result))









'''
Rebalancing the height of the tree
'''
def rebalance(h_min, h_max, min_length, max_length):
    if min_length>max_length:
        heappush(h_max,-heappop(h_min))
        min_length -= 1
        max_length += 1
    else:
        heappush(h_min,-heappop(h_max))
        max_length -= 1
        min_length += 1
    return min_length,max_length

h_min = []
h_max = []
min_length = 0
max_length = 0
med = 0
for _ in range(int(input())):
    n = int(input())
    if min_length == 0 or n<=med:
        heappush(h_min,-n)
        min_length+=1
    elif n>med:
        heappush(h_max,n)
        max_length+=1
    if abs(min_length-max_length) >= 2:
        min_length,max_length = rebalance(h_min,h_max,min_length,max_length)
    if min_length>max_length:
        med = -h_min[0]
    elif min_length<max_length:
        med = h_max[0]
    else:
        med = ((-h_min[0]+h_max[0])/2.0) 
    print (int(med))