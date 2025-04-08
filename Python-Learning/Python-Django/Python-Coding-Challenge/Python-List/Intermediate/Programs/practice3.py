nums = [10,20,30,20,10,40,50]

# unique_nums = list(set(nums)) 
# print(unique_nums)


# Maintaing the order (it will actually sort)
unique_nums = []

for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)
print(unique_nums)
    