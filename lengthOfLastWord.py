class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or all(i == ' ' for i in s):
            return 0
        else:
            words = s.split()
            return(len(words[-1]))
