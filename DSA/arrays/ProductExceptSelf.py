'''
        [1, 2, 3, 4]
        pre = 1, 2
        res = [1*1, 1*1, 1*2, 2*3] = [1, 1, 2, 6]
        post = 1
        res = [1, 1, 2, 6] => [1*]

 the idea is for each element, we calculate the prefix and then 
 the postfix products and multiply them together

'''

def productExceptSelf(self, nums: List[int]) -> List[int]:
    '''
    [1, 2, 3, 4]
    pre = 1, 2
    res = [1*1, 1*1, 1*2, 2*3] = [1, 1, 2, 6]
    post = 1
    res = [1, 1, 2, 6] => [1*]
    '''
    res = [1] * len(nums)
    pre = 1
    for i in range(len(nums)):
        res[i] = pre
        pre *= nums[i]
    post = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= post
        post *= nums[i]
    
    return res