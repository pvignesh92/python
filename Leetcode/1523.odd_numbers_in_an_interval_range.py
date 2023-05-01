
# Common Apporach but consumes time and memory - Failure with Timeout
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        cnt = 0
        for i in range(low, high+1):
            if i%2 != 0:
                cnt += 1
        return cnt


# Memory and Time efficient Approach - Accepted Solution
class Solution:
    import math
    def countOdds(self, low: int, high: int) -> int:
        cnt = 0
        diff = high - low
        if low%2 != 0 and high%2 != 0:
            cnt = math.ceil(diff/2 + 1)
        else :
            cnt = math.ceil(diff/2)
        return cnt