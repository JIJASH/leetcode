class Solution:
    def countLargestGroup(self, n):
        dp = {
            0 : 0
        }
        counter = [0] * 37

        for i in range(1,n+1):
            dp[i] = i % 10 + dp[ i // 10 ]
            counter[dp[i]] += 1
        maximum = max(counter)
        return counter.count(maximum)
        