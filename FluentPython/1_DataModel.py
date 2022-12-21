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
