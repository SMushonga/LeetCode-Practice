class Solution(object):
    def twoSum(self, nums, target):
        original_list = list(nums)
        nums.sort()
        pointer_left = 0
        pointer_right = len(nums) - 1
        sum = 99999
        while sum != target:
            sum = nums[pointer_left] + nums[pointer_right]
            if sum > target:
                pointer_right -= 1
            elif sum < target:
                pointer_left += 1
        final_index_left = original_list.index(nums[pointer_left])
        final_index_right = original_list.index(nums[pointer_right])
        if final_index_left == final_index_right:
            final_index_right = original_list.index(nums[pointer_right], final_index_left+1)
        return [final_index_left, final_index_right]