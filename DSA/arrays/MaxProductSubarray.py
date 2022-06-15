'''
we keep track of the current min and max. this way, we can account for negative nums
in the array. the min is jus thte max negative value so if there is a following neg
that makes the whole thing positive, we'll have the value stored already in the 
min. we then compare these values to the current max. 

'''

def maxProduct(self, nums: List[int]) -> int:
#         keep track of max product for negative and positive
    res = max(nums)
    curMin, curMax = 1, 1
    
    for i in nums:
        tmp = curMax * i
        curMax = max(i * curMax, i * curMin, i)
        curMin = min(tmp, i * curMin, i)
        res = max(curMax, res)
    return res