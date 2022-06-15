'''
The idea behind this is to use enumerate to get the index and the value.
You store the value you're searching for for each element and if its there you return the 
index from the map.

'''

def twoSum(self, nums: List[int], target: int) -> List[int]:
    
    trackingSet = {}
    
    for i,j in enumerate(nums):
        if j in trackingSet:
            return [trackingSet[j], i]
        else:
            trackingSet[target-j] = i