class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = nums.sort()
        if all(for )
        for x in nums:
            if target 
        tups = enumerate(nums)
        numdic = dict(tups)
        for key in numdic:
            num = numdic[key]
            diff = target - num
            key_list = [k for k, v in numdic.items() if v == diff]
            for ind in key_list:
                if ind != key:
                    return key, ind
            
            
