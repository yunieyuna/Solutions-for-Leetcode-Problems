# https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        # https://leetcode-cn.com/problems/count-primes/solution/pythonzui-you-jie-fa-mei-you-zhi-yi-liao-ba-by-bru/
        
        if n < 2:
            return 0
        
        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0
        
        for i in range(2, int(n**0.5) + 1):
            if isPrime[i]:
                isPrime[i * i:n:i] = [0] * ((n - 1 - i*i) // i + 1)
                
        return sum(isPrime)
        
"""
Runtime: 116 ms, faster than 97.42% of Python3 online submissions for Count Primes.
Memory Usage: 36.1 MB, less than 58.62% of Python3 online submissions for Count Primes.
"""
