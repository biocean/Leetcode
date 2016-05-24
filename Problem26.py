__author__ = 'aa23314'

class Solution26(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        result = []
        result.append(nums[0])
        i = 1
        while i< len(nums):
            if nums[i] != result[-1]:
                result.append(nums[i])
            i+=1
        return len(result)

a = Solution26()
print(a.removeDuplicates([1,1,3,3,4]))