class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(filter(str.isalnum, s)).lower()
        revString = string[::-1]
        return string == revString
