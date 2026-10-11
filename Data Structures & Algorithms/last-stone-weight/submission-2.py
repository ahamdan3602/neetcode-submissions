import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, stone in enumerate(stones):
            stones[i] = -stone

        heapq.heapify(stones)  

        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return 1      

        while len(stones) > 1:
            x = -(heapq.heappop(stones))
            y = -(heapq.heappop(stones))
            if x == y:
                continue
            else:
                print(x, y)
                new_weight = (y - x)
                heapq.heappush(stones, new_weight)
    


        if len(stones) > 0:
            return -stones[0]
        return 0

            
        