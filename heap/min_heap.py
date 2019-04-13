from heapq import heappop, heappush, heapify
# heappop => pop and returns the smallest element from the heap
# heappush => push the value item onto the heap invariant 
# heapify => transforms list into heap, in place and in linear time

# class to implement the min heap
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self,i):
        return (i-1)//2

    def insertKey(self, K):
        heappush(self.heap, K)
    
    def decreaseKey(self, i, newVal):
        self.heap[i] = newVal
        