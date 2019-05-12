class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = 0
        y = 0
        current = 1
        directions = [(-1, 0), (0, 1), (1,0), (0,-1)]
        for i in range(4):
            for s in instructions:
                if s == "G":
                    x += directions[current][0]
                    y += directions[current][1]
                elif s == "L":
                    current = (current +3) % 4
                else:
                    current = (current+1) % 4
            if x == 0 and y == 0:
                return True
        return False
