# filter()

marks = [50,70,80,65,75,78,79,90,95,98,97]

merit_results= list(filter(lambda x: x >= 80, marks))
print(merit_results)