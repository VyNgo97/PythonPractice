'''
What issue does the linked list solve?
Array insertions run in O(n) because we can insert an element at a point but
then we must shift the rest of the array over one. When we call array.insert(),
our code will shift the following elements of the specified index down to make space 
then it will insert the element.

In linked lists, since data does not have to be stored in contiguous memory locations,
we don't have the same issues. Linked lists contain nodes that contain a value and the 
memory address of the NEXT value in the linked list. It looks like this:

0x00500: [1 | 0x00A1] -> 0x00A1: [2 | 0x00C5] -> 0x00C5: [3 | null]

Now, when we want to insert an element at any point in the list, we can just modify 
the links to point to the new address. There is no shifting or making space like an array.
It is just modifying a single pointer of the previous element to point to it and making
sure the pointer for that new node points to the next element in the list. All following
elements in the linked list stay the same.

Insertions and deletions at the beginning of a linked list => O(1)
Insertions and deletions at the end => O(n) 
Indexing => O(n)
Insert/Delete at mid => o(n)

^^ This is because linked lists are linear data structures that require you to
traverse them to get to a specific element. You can't do random access like with arrays
because you don't know where the next element is in memory.

Benefits:
    1. You don't need to preallocate space
    2. Insertion is easier

Double linked lists:

We now have a link to the next AND the previous element
0x00500: [null| 1 | 0x00A1] <--> 0x00A1: [0x00500| 2 | 0x00C5] <--> 0x00C5: [0x00A1| 3 | null]

In code, the only real difference is now we have an attribute called prev that points to the previous node
'''

from typing import Any

class Node:
    def __init__(self, data: Any=None, next: Any=None, prev: Any=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data: Any):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data: Any):
        node = Node(data, None)
        if self.head is None:
            self.head = node
            return
            
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node
    
    def print(self):
        if self.head is None:
            print("Empty list")
            return
        itr = self.head
        llist = ''
        while itr:
            llist += str(itr.data) + '--->'
            itr = itr.next
        
        print(llist)
    
    def insert_values(self, data_list: list[Any]):
        self.head = None
        for item in data_list:
            self.insert_at_end(item)
    
    def get_length(self):
        counter = 0
        itr = self.head
        while itr:
            counter+=1
            itr = itr.next
        return counter

    def reverse(self):
        if self.head is None:
            print("Empty list")
            return
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            if prev:
                print(f'{curr.data} now points to {prev.data}')
            prev = curr
            curr = nxt
        return self
    
    def remove_at(self, idx: int):
        if idx < 0 or idx > self.get_length():
            raise Exception(f'No value at index {idx}')

        if idx == 0:
            self.head = self.head.next
            return

        count = 1
        itr = self.head

        while itr:
            if count == idx:
                itr.next = itr.next.next
                return
            count+=1
            itr = itr.next

    def insert_at(self, idx: int, val: any):
        if idx < 0 or idx > self.get_length() + 1:
            raise Exception('Invalid index')
        
        if idx == 0:
            self.insert_at_beginning(val)
        return

        count = 1
        itr = self.head
        while itr:
            if count == idx:
                node = Node(val, itr.next)
                itr.next = node
                return
            count+=1
            itr = itr.next
        
    def insert_after(self, idx, val):
        if idx == 0 or idx > self.get_length():
            raise Exception('Invalid index')
        
        if idx == self.get_length() - 1:
            self.insert_at_end(val)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == idx:
                node = Node(val, itr.next)
                itr.next = node
                return
            count+=1
            itr = itr.next

    def remove_by_value(self, val):
        if self.head == None:
            return

        if self.head.data == val:
            self.head = self.head.next
            return

        itr = self.head
        while itr and itr.next:
            if itr.next.data == val:
                itr.next = itr.next.next
            itr = itr.next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, val):
        if self.head == None:
            node = Node(val, self.head, None)
            self.head = node
        else:
            node = Node(val, self.head, None)
            # when adding to the front, we take the current head and point it to the new node
            self.head.prev = node
            # now our new node is the new head
            self.head = node

    def insert_at_end(self, val):
        last_node = self.get_last_node()
        if self.head == None:
            node = Node(val, None, None)
            self.head = node
        else:
            node = Node(val, None, last_node)
            last_node.next = node

    def print_backwards(self):
        itr = self.get_last_node()
        llist = ''
        while itr:
            llist += str(itr.data) + '<--->'
            itr = itr.prev
        print(llist)

    def print_forwards(self):
        llist = ''
        itr = self.head
        while itr:
            llist += str(itr.data) + '<--->'
            itr = itr.next
        print(llist)
    
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_beginning(1)
    linked_list.insert_at_beginning(2)
    linked_list.insert_at_beginning(3)
    linked_list.insert_at_end(6)
    linked_list.insert_values([1,2,3,4,5])
    # linked_list.reverse()
    linked_list.print()
    # linked_list.remove_at(2)
    linked_list.insert_at(0, 6)
    linked_list.print()
    linked_list.insert_after(5, 12)
    linked_list.remove_by_value(6)
    linked_list.print()
    print('=================================')
    doubly_list = DoublyLinkedList()
    doubly_list.insert_at_beginning(1)
    doubly_list.insert_at_beginning(2)
    doubly_list.insert_at_beginning(3)
    doubly_list.insert_at_end(5)
    doubly_list.print_backwards()
    doubly_list.print_forwards()
    test = {'test': 1}
    word = 'hello'
    print(ord('b'))