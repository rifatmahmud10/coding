from collections import defaultdict


def majority_element(nums):

    n = len(nums)
    hsh = defaultdict(int)

    for num in nums:
        hsh[num] += 1
    m = n//2
    for key, value in hsh.items():
        if value > m:
            return key


print(majority_element([1, 1, 2, 1, 21, 34, 1, 2, 1]))
