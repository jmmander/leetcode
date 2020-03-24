class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        rev = x_str[::-1]
        if rev == x_str:
            return True
        else:
            return False
        
