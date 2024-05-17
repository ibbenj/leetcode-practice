# https://leetcode.com/problems/the-kth-factor-of-n/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factorCnt = 0
        factors = []

        for i in range(1,floor(sqrt(n))+1):
            if n % i == 0:
                factorCnt += 1
                factors.append(i)

                if factorCnt == k:
                    return i

        totFactors = 0
        if floor(sqrt(n))**2 == n:
            totFactors = (len(factors)-1)*2+1
        else:
            totFactors = len(factors)*2

        if k > totFactors:
            return -1
        else:
            oppFactor = factors[totFactors-k]
            return round(n/oppFactor)

# Runtime O(sqrt(n))
# Spacetime O(sqrt(n))

# Trick is that each factor of n has a corresponding factor (expect for the sqrt if its an integer) e.g. in 16 we have 1,16 2,8 4,4.
# We can use this fact to only have to check the first sqrt(n) integers for factors and for the rest we just divie n by each factor