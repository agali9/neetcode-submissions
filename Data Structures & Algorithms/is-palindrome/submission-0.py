class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join(ch for ch in s if ch.isalnum())
        s1 = s1.lower()
        for i in range(len(s1)):
            ch1 = s1[i]
            ch2 =  s1[len(s1)-1-i]
            if ch1 != ch2: return False
        return True