
# Find the duplicates numbers in the list, for that we're going to use the for loop

def find_duplicates(num):
    return list(set([x for x in num if num.count(x) > 1]))

print(find_duplicates([1,2,1,2,3,4]))