def majority_element(nums):
    n = len(nums)
    nums.sort()
    return nums[n//2]


print(majority_element([3, 4, 5, 5, 5, 6, 7, 5, 5]))
