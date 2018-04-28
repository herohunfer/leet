class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        for index, val in enumerate(graph):
            for i in range(len(val)):
                for j in range(i+1, len(val)):
                    if val[j] in graph[val[i]]:
                        return False
        return True