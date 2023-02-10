def has_33(nums):
    for x in range(len(nums) - 1):
        if nums[x] == 3 and nums[x + 1] == 3:
            return True
    else: # (nums[x] == 3 and nums[x + 1] != 3) or (nums[x] != 3 and nums[x + 1] == 3)
        return False    

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))