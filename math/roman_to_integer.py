class Solution:
    def romanToInt(self, s: str) -> int:
        encodings = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        val = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and ((s[i] == "I" and (s[i + 1] == "X" or s[i + 1] == "V")) or (
                    s[i] == "X" and (s[i + 1] == "L" or s[i + 1] == "C")) or (
                                           s[i] == "C" and (s[i + 1] == "D" or s[i + 1] == "M"))):
                val = val + encodings[s[i + 1]] - encodings[s[i]]
                i = i + 2
            else:
                val = val + encodings[s[i]]
                i = i + 1
        return val


X = Solution
print(X.romanToInt(X, "LVIII"))