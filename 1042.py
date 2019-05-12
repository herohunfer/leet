class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        m = {}
        for p in paths:
                i = min(p[0], p[1])
                j = max(p[0], p[1])
                if j-1 in m:
                    m[j-1].append(i-1)
                else:
                    m[j-1] = [i-1]
        return self.dfs(N, [], m)
    def dfs(self, N, result, m):
        if len(result) == N:
            return result
        avaiable = set([1,2,3,4])
        current = len(result)
        if current in m:
            for i in m[current]:
                avaiable.discard(result[i])
        for i in avaiable:
            result.append(i)
            self.dfs(N, result, m)
            if len(result) == N:
                return result
            result.pop()
        return result
