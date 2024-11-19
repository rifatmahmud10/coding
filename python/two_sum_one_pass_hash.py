def two_sum(nums, target):
    n = len(nums)
    hash_table = {}
    for i in range(n):
        complement = target - nums[i]
        if complement in hash_table:
            return [i, hash_table[complement]]
        hash_table[nums[i]] = i


# Taking input for the list of numbers
nums = list(map(int, input('Enter the numbers separated by space: ').split()))
target = int(input('enter the target'))
print(two_sum(nums, target))
