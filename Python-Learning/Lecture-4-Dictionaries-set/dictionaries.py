# info = {

#     "name" : "HarendraBarot",
#     "subjects" : ["Python","Java", "C#"],
#     "topics" : ("dict","set"),
#     "age" : 29,
#     "is_adult" : True,
#     "marks" : 94.9
# }

# # print(info["fname"])
# # print(info["subjects"])
# # print(info["topics"])
# # print(info["age"])

# null_dict = {}
# null_dict["name"] = "Haridan"
# print(null_dict)

# info["name"] = "Harry"  #overwrite # we can assign integer, float or boolean data types
# info["surname"] = "Barot"
# print(info)




### Nested Dictionary 


student = {
    "name" : "Harry",
    "age" : 29,
    "state" : "Gujarat",
    "addres": "Gandhidham",
    "pincode" : 370201,

    "score":  {
       "chem" : 98,
       "phy" : 97,
       "math" : 95

    }


}

# student["name"] = "Harendra"
# print(student["score"]["chem"])
# print(list(student.keys()))
# print(student.values())


# print(list(student.values()))

# pairs = (list(student.items()))
# print(pairs[1])


# print(student.get("age"))
# print(student.get("pincode"))
# print(student.get("pincode1"))


# student.update({"contact" : 8849964295})
# print(student)


new_dict = {"contact" : 8849964295, "email" : "harendrabarot19@gmail.com"}
student.update(new_dict)

print(student)