class Solution:
    def countPrimes(self, n: int) -> int:
        nums = list(range(2, n))
        primes = 0
        k = 0
        while k < len(nums):
            last_prime = nums[k]
            primes = primes+1
            multiples = (n-1)//last_prime
            k = k+1
            if k > len(nums)-1:
                break
            while nums[k] == 0:
                k = k+1
                if k > len(nums) - 1:
                    break
            for i in range(1, multiples+1):
                nums[last_prime*i-2] = 0
        return primes

X = Solution
X.countPrimes(X, 10)