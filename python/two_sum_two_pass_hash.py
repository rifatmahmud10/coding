def two_sum(nums, target):
    hash_table = {}
    n = len(nums)

    for i in range(n):
        hash_table[nums[i]] = i
    for i in range(n):
        complement = target - nums[i]
        if complement in hash_table and hash_table[complement] != i:
            return [i, hash_table[complement]]
    return []


# Taking input for the list of numbers
nums = list(map(int, input('Enter the numbers separated by space: ').split()))
target = int(input('enter the target'))
print(two_sum(nums, target))
