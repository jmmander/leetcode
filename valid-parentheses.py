class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        valid = ["[]","()","{}"]

        if len(s) == 0:
            return True
        elif len(s)%2 != 0:
            return False
        else:
            match = next((x for x in valid if x in s), False)
            if match != False:
                new = s.replace(match,"", 1)   
                return self.isValid(new)
                
