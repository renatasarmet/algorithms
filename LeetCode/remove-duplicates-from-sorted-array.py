# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums)>0):
            size = 1
        else:
            size = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[size] = nums[i]
                size += 1
        return size
        