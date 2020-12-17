from fractions import gcd
from functools import reduce


def find_gcd(list):
    x = reduce(gcd, list)
    return x


class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """

        freq = {} 
        for card in deck:
            if (card in freq): 
                freq[card] += 1
            else: 
                freq[card] = 1
        freq_vals = freq.values()
        x = min(freq_vals)
        if x <=1:
            return False
        greatest = find_gcd(freq_vals)
        if greatest <= 1:
            return False
        return True
