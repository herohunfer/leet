class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones)> 1:
            i = stones.pop()
            j = stones.pop()
            remain = i-j
            if remain > 0:
                l = 0
                r = len(stones)-1
                flag = False
                while l <= r:
                    middle = l+ (r-l)//2
                    if stones[middle]> remain:
                        r = middle-1
                    elif stones[middle] < remain:
                        l = middle+1
                    else:
                        stones.insert(middle, remain)
                        flag = True
                        break
                if not flag:
                    stones.insert(l, remain)
            #print(stones)
        return stones[0] if len(stones)> 0 else 0
