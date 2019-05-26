class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        total = sum([customers[i] if not grumpy[i] else 0 for i in range(len(customers))])
        # print(total)
        current = sum([customers[i] if grumpy[i] else 0 for i in range(X)])
        # print(current)
        maximum = current
        # print("current=",current)
        for i in range(X, len(customers)):
            current += (customers[i] * grumpy[i]) - (customers[i-X] * grumpy[i-X])
            # print("current=",current)
            if current > maximum:
                maximum = current
        return total + maximum
