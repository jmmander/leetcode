from collections import OrderedDict 

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
   
        roms = {"I": 1, "V": 5, "X": 10, "L":50, "C":100, "D":500, "M":1000}
        total = 0
        s = s.encode("utf-8")
        slist = list(s)    
        while len(slist) != 0:
            first = slist[0]
            if len(slist) > 1:
                sec = slist[1]
                if roms[sec] > roms[first]:
                    total = total + roms[sec] - roms[first]
                    slist.remove(first)
                    slist.remove(sec)
                else:
                    total = total + roms[first]
                    slist.remove(first)
            else:
                total = total + roms[first]
                return total
               
        return total
  
