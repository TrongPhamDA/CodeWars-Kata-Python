'''
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
'''

# def count_bits(n):
#     count = 0
#     while n > 0:
#         if n % 2 == 1: count += 1
#         n //= 2
#     return count

# def count_bits(n):
#     count = 0
#     while n > 0:
#         count += n % 2
#         n //= 2
#     return count

# def count_bits(n):
#     return '{:b}'.format(n).count('1')

def count_bits(n):
    return bin(n)[2:].count('1')

print(count_bits(0)== 0)
print(count_bits(4) == 1)
print(count_bits(7) == 3)
print(count_bits(9) == 2)
print(count_bits(10) == 2)