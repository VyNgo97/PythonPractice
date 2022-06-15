'''
idea is that for each element in the first position, we want to use 2 pointers to 
meet the condition for the other two elements.
'''

def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    
    for i, v in enumerate(nums):
        if i > 0 and v == nums[i-1]:
            continue
        
# for each value in the first position, we use 2 pointers to figure out the last two values
        l,r = i + 1, len(nums) - 1
        
        while l < r and r < len(nums):
            threeSum = v + nums[l] + nums[r]
            if threeSum > 0:
                r-=1
            elif threeSum < 0:
                l+=1
            else:
                res.append([v, nums[l], nums[r]])
                l+=1
# now we want to see if there are any other [l, r] combos that satisfy the condition with the same first value
                while nums[l] == nums[l-1] and l < r:
                    l+=1
    
    return res