class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for ch in s:
            if ch.isalnum():
                res += ch.lower()

        b = res[::-1]

        if res == b :
            return True
        else :
            return False 
        