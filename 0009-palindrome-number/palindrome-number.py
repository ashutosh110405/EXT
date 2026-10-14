class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        n = x
        while n > 0:
            digit = n % 10
            rev = rev * 10 + digit
            n = n // 10
        if rev == x:
            return True
        else:
            return False