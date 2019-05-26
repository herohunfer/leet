class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        
        total = sum([customers[i] if not grumpy[i] for i in range(len(customers))])
        current = sum([customers[i] if grumpy[i] for i in range(X)])
        maximum = current
        for i in range(X, len(customers)-X+1):
            current += (customers[i] * grumpy[i]) - (customers[i-X] * grumpy[i])
            if current > maximum:
                maximum = current
        return total + maximum
