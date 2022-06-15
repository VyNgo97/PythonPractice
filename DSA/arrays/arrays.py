'''Integers are stored in 4 bytes so an array's memory address would look like:
    list[0] = 0x00500
    list[1] = 0x00504
    list[2] = 0x00508
    
    In Python, lists are stored in contiguous blocks to make indexing fast.
    Element = InitialLocationAtIndex0 + (4 bytes * IndexWanted) 

    Big O -
        Lookup by index = O(1) list[1]
        Lookup by value = O(n) for i in list
        Traversal = O(n) for i in list
        Insertion at start = O(n) due to shift- list.insert(index, value)
        Deletion at start = O(n) due to shift- list.remote(index) 

        Insert/Delete at mid = O(n)

        Insert/Delete at the END of a list runs in O(1) amortized
    
    In dynamic arrays, when you expand the array by adding new elements it will automatically
    allocate space of size (currentArraySize + currentArraySize * 2) and 
'''

from dataclasses import dataclass


lst = [1, 2, 3, 4, 5]

# print(dir(lst))
'''
Below are all the standard (non dunder) python methods

['append', 'clear', 'copy', 'count', 'extend', 
'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''

expenses = [2200, 2350, 2600, 2130, 2190]

# sum of list
total = sum(expenses[:3])
print(total)
# adding an element to the list
expenses.append(1980)
# edit a single element in list
expenses[3] = expenses[3] - 200

heros=['spider man','thor','hulk','iron man','captain america']

# first choose an index then object to insert
heros.insert(3, 'black panther')

# replace 2 contiguous elements with 1
heros[1:3]=['doctor strange']

# return list of heros with condition
heros = [hero for hero in heros if hero not in ['thor', 'hulk']]

# print(heros)

odds = []
for i in range(1, 100):
    if i % 2 != 0:
        odds.append(i)
# print(odds)

# adds 2 iterables together
heros.extend(expenses)

@dataclass
class Obj:
    name: str
    age: int

    def changeAge(self, new_age):
        self.age = new_age

lst_a = [Obj('vy', 24), Obj('jamie', 24)]
# creates a shallow copy -> same reference in memory still so changes in copy affects original
lst_b = lst_a.copy()

print(lst_b)

lst_a[1].changeAge(25)
# althought the LIST is a copy, the objects (disregard primitives) in the list are just references
# to the same object so changing the value of the object in list a changes it in list b
# to circumvent this, use a deepcopy() to make a copy of objs in list as well
print(lst_b)



