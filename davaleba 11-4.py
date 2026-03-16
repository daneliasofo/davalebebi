nums = [8, 3, 5, 1, 9, 4]

min_index = nums.index(min(nums))
max_index = nums.index(max(nums))

nums[min_index], nums[max_index] = nums[max_index], nums[min_index]

print(nums)