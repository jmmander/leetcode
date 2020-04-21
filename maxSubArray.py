class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best = 0
        maxi = 0
        if any(i > 0 for i in nums):
            for i in range(len(nums)):
                current = nums[i]
                contin = best + nums[i]
                best = max(current, contin)
                if best > maxi:
                    maxi = best
        else:
            maxi = max(nums)

            
        return maxi
            
