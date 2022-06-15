'''
here all we are doing is checking if for each element, if it is greater alone or added
to the previous sum. if it is greater than we change the curr value and do the
same comparison to the max

'''
def maxSubArray(self, nums: List[int]) -> int:
    res = nums[0]
    curr = res
    
    for i in range(1, len(nums)):
#   think of nums[i] being the left pointer and curr + nums[i] being the right pointer here
        curr = max(nums[i], curr + nums[i])
        res = max(res, curr)
    return res