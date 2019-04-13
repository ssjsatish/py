# import heapq
# a = [1,2,3,4,5,6,7,8,9,10]
# b = [1,2,3,4,5,6,7,8,9,10]
# heapq.heapify(a)
# heapq.heapify_max(b)
# print(heapq.heappop(minheap))
# print(heapq.heappop(maxheap))

'''
import heapq
class MaxHeap(object):
    def __init__(self):
        self.h = []
    def heappush(self, x):
        heapq.heappush(self.h, x)
    def heappop(self):
        return heapq.heappop(self.h)
    def __getitem__(self, i):
        return self.h[i]
    def __len__(self):
        return len(self.h)
    
class MaxHeap(MinHeap):
    def heappush(self,x):
        heapq.heappush(self.h, )
'''
import heapq
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
heapq.heapify(arr)             # for a min heap
print(arr)
heapq._heapify_max(arr)        # for a maxheap!!
print(arr)