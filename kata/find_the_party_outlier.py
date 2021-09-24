'''
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
'''

# def find_outlier(integers):
#     evens = []
#     odds  = []
#     for num in integers:
#         if num % 2 == 0: evens.append(num)
#         else: odds.append(num)
#     return evens[0] if len(evens) == 1 else odds[0]

# def find_outlier(integers):
#     odds  = [num for num in integers if num % 2 != 0]
#     evens = [num for num in integers if num % 2 == 0]
#     return odds[0] if len(evens) > len(odds) else evens[0]

def find_outlier(integers):
    parity = [num % 2 for num in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]

print(find_outlier([2, 4, 6, 8, 10, 3]) == 3)
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) == 11)
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]) == 160)