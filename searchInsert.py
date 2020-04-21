class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.append(target)
        snew = sorted(list(set(nums)))
        return snew.index(target)
