class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -2 ** 31 <= x <= (2 ** 31)-1:
            if x > 0:
                s = list(str(x))
                s.reverse()
                fin = int("".join(s))
                if -2 ** 31 <= fin <= (2 ** 31)-1:
                    return fin
                else:
                    return 0
            elif x < 0:
                s = list(str(x))[1:]
                s.reverse()
                fin = -1*int("".join(s))
                if -2 ** 31 <= fin <= (2 ** 31)-1:
                    return fin
                else:
                    return 0
            else:
                return 0
        else:
            return 0




X = Solution
print(X.reverse(X, 1534236469))