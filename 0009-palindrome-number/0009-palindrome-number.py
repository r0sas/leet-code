class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        for i in range(int(len(num_str)/2)):
            if num_str[i] != num_str[len(num_str)-i-1]:
                return False
        return True