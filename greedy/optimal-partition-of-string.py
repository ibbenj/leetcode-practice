class Solution:
    def partitionString(self, s: str) -> int:
        partitionCnt = 1
        subStrLetters = set()

        for letter in s:
            if letter in subStrLetters:
                partitionCnt += 1
                subStrLetters.clear()

            subStrLetters.add(letter)

        return partitionCnt

# O(n) runtime
# O(n) spacetime
# Uses greedy algorithm and beats 90.0% of python3 users for runtime