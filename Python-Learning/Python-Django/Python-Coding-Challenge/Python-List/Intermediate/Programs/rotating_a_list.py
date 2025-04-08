#  Rotating a List

nums = [1, 2, 3, 4, 5]

# Rotate right by 2 positions
rotated = nums[-2:] + nums[:-2]
print(rotated)  # [4, 5, 1, 2, 3]
