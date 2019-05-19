class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        smallest = 3000
        path = set()
        path.add(stones[0])
        path.add(-stones[0])
        for stone in stones[1:]:
            new_path = set()
            for item in path:
                val1 = item + stone
                new_path.add(val1)
                val2 = item-stone
                new_path.add(val2)
            path = new_path
        for val in path:
            if abs(val) < smallest:
                smallest = abs(val)
        return smallest
