'''
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''


# def letterCombinations(digits:str):
#     # each combination is only as long as len(digits) 2-> 'a', 'b', 'c' 3 -> 'd', 'e', 'f' => 'ab', 'ae', 'af'...
#     digit_to_letter = {'2': ['a', 'b', 'c'], '3':['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}


    
#     def ans(digits, digit_to_letter):

#         if len(digits) == 0:
#             return []

#         if len(digits) == 1:
#             return digit_to_letter[digits]

#         return [i + j for i in digit_to_letter[digits[0]] for j in ans(digits[1:], digit_to_letter)]

#     return ans(digits, digit_to_letter)

# print(letterCombinations('234'))

# sequence = 1, 1, 2, 3, 5, 8, 13
def fibonacci(num):
    if num == 0:
        return num
    elif num == 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(6))