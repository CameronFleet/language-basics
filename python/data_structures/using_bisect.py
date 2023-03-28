import bisect

nums = [1, 5, 10, 15, 30, 35]

print(f"nums: {nums}; bisect_right(6): {bisect.bisect(nums, 6)}")
print(f"nums: {nums}; bisect_left(6): {bisect.bisect_left(nums, 6)}")

print(f"nums: {nums}; bisect_right(5): {bisect.bisect(nums, 5)}")
print(f"nums: {nums}; bisect_left(5): {bisect.bisect_left(nums, 5)}")

bisect.insort_right(nums, 3)

print(f"nums: {nums}; bisect_right(6): {bisect.bisect(nums, 6)}")
print(f"nums: {nums}; bisect_left(6): {bisect.bisect_left(nums, 6)}")
