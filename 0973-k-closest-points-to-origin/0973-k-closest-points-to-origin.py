import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap=[]
        for x,y in points:
            distance=x*x+y*y
            heapq.heappush_max(heap,(distance,[x,y]))
        while len(heap)>k:
            heapq.heappop_max(heap)
        ans=[]
        for distance , points in heap:
            ans.append(points)
        return ans
        