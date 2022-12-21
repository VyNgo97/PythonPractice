'''
given an array [1, 2, 3, 0, 5, 3]

start at index 0 and move through out the array based on the value at that index.
for example, at index 0 you can move one space forward or backwards. always move 
forward at the beginning really. then its 0 + 1 which lands on 2, you can then move forward
or backwards 2 spaces. do this and determine if you run into a 0. sometimes it is False even when a 0 is present. i.e. [7, 8, 0]

'''

def find_zero(lst: List[int]) -> bool:
    '''
    
    '''

    visited = {}
    curr = 0

    while True:
        if curr in visited:
            if visited[curr] == 0:
                curr+=visited[curr]
            elif visited[curr] == 1:
                return False

        