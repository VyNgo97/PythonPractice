'''
This one is straightforward, we add each value to a set and if the set already
contains that value we return true. we can do something similar by comparing a sorted 
list with the set of that list
'''

def containsDuplicate(self, nums: List[int]) -> bool:
    val = set()
    for i in nums:
        if i in val:
            return True
        val.add(i)
    return False