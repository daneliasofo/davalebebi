nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

avg = sum(nums) / len(nums)

for x in nums:
    if x > avg:
        print(x)