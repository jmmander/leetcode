class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        final = []
        whole = [str(num) for num in digits]
        num = "".join(whole)
        num = int(num) + 1
        for i in str(num):
            final.append(int(i))
        return final
        
