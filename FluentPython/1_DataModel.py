"""
What are special methods and when do we use them?

Special methods or dunder methods in Python are wrapped in double underscores like `__getitem__()`. The syntax obj[key] is supported by the `__getitem__()` dunder method that is
when we use `obj[key]`, the interpreter calls `obj.__getitem__(key)`. Many of thse dunder methods are defaulted when you create a class but adding it to your own class allows
you to use features that are supported by the base language. By this I mean we can customize `__repr__()` for prettier printing or add the `__getitem__()` dunder method to support use `obj[key]` notation.

"""

class TestObj:
    name: str

    def __init__(self, name):
        self.name = name
    
    def __repr__(self) -> str:
        return f"Object Name: {self.name}"
    

new_obj = TestObj("Vy")
# print(new_obj.__repr__())

""" Pythonic Card Deck """
import collections

# Creates a simple class to represent a card. Cards only have a rank and suit so this works fine.
# This is used when there is a class that is only a bundle of attributes and no custom methods. We can extend the attributes by adding to the list.
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # The book uses 'spades diamonds clubs hearts'.split() <- easy way but not as clear about the type 
    suits = ['spades', 'diamonds', 'club', 'hearts'] 

    def __init__(self) -> None:
        # creates a deck of cards of type namedtuple with suit and rank -> similar to a nested for loop
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]