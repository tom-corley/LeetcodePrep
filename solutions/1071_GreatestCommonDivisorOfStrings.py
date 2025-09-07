class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def check_divides(divisor, string):
            if len(string) % len(divisor) != 0:
                return False

            i = 0
            while i < len(string):
                if string[i:i+len(divisor)] != divisor:
                    return False
                i += len(divisor)
            return True

        str1_divisors = []
        divisor = ""
        for i in range(len(str1)):
            divisor += str1[i]
            if check_divides(divisor, str1):
                str1_divisors.append(divisor)

        ans = ""
        for divisor in str1_divisors:
            if check_divides(divisor, str2):
                if len(divisor) > len(ans):
                    ans = divisor

        return ans