class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        temp = [-gift for gift in gifts]
        heapq.heapify(temp)
        for i in range(k):
            gift = heapq.heappop(temp) * -1
            gift = int(sqrt(gift))
            heapq.heappush(temp, gift * -1)
        return sum(temp) * -1