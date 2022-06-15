def func(x):
    return x+5

# print(func(2))

func2 = lambda x: x+5

test_dict = {'a': 1, 'b': 4, 'c': 2}
# key should be a function or callable that thats a single arg and returns the key we sort by
# in this first example, it returns the value which is what we are sorting by 
print(sorted(test_dict, key=lambda x: test_dict[x], reverse=True))
# in this second example, it returns a lowercase string that we are sorting by
print(sorted("This is a test string from Andrew".split(), key=str.lower))
# we can think of it as applying that callable to all elements in our list or dict and then sorting by that value

