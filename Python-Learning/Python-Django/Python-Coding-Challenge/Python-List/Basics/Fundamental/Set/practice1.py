
# 1. Find Common Elements Between Two Lists

# list1 = [1,2,3,4,5]
# list2 = [4,5,6,7,8]

# common = list(set(list1) & set(list2))  # & is the intersection operator — it finds values present in both sets.
# print('Common numbers in list are:', common )



# # 2. Remove Duplicates From a List

# items = [1,2,3,4,4,5,5]
# unique_items = list(set(items))   # set() automatically filters out all duplicates.
# print('Without duplicates:', unique_items)


# Check if a String Contains All Vowels

vowels = set('aieou')
user_input = input('Enter a sentence:').lower()


if vowels.issubset(set(user_input)):    # issubset() checks if all vowels are included in the user’s input.
    print('Input contains all the vowels')
else:
    print('Not all vowels are present')



