class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for point in points:
            x, y = point
            dist = math.sqrt(x*x + y*y)
            heapq.heappush(heap, [dist,x,y])
        res = []
        for i in range(k):
            arr = heapq.heappop(heap)
            res.append([arr[1],arr[2]])
        return res