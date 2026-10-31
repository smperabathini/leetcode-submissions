class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        for stone in stones:
            heapq.heappush(heap, -1 * stone)
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if x < y:
                heapq.heappush(heap,-y+x)
        return -1 * heap[0] if heap else 0