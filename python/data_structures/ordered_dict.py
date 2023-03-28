from collections import OrderedDict

# Implemented with a doubly linked list
nums = OrderedDict()

# Maintains order of insertion
nums['a'] = 3
nums['b'] = 5
nums['f'] = 2
nums['c'] = 4
print(nums)

# O(1)
nums.move_to_end('a') 
print(nums)

# O(1)
print(nums.popitem(last=False))
print(nums)