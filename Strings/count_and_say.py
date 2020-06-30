class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 1:
            return "1"
        else:
            x = self.countAndSay(X, n-1)
            n_digits = list(x)
            out = []
            i = 0
            while i < len(n_digits):
                count = 0
                current = n_digits[i]
                while i < len(n_digits) and int(n_digits[i]) == int(current):
                    count = count+1
                    i = i + 1
                out.append(str(count))
                out.append(str(current))
            c_s = "".join(out)
            return c_s


X = Solution
print(X.countAndSay(X, 5))