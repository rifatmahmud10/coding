def two_Sum(nums, target):
    n = len(nums)

    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]


# Taking input for the list of numbers
nums = list(map(int, input('Enter the numbers separated by space: ').split()))
target = int(input('enter the target'))
print(two_Sum(nums, target))
