# Declare a common_elements function that accepts a dictionary
# It should return a list with all of the elements that are found
# as both a key and a value in the dictionary
#
# HINT: Use the in operation to check for inclusion in a view or list object
#
# EXAMPLE:
# my_dict = {
#   "A": "K",
#   "B": "D",
#   "C": "A",
#   "D": "Z"
# }
#
# common_elements(my_dict) => ["A", "D"]

my_dict = {
    "A": "K",
    "B": "D",
    "C": "A",
    "D": "Z"
}


# def ccommon_elements(my_dict):
#     results = []

#     for string in my_dict.keys():
#         for item in my_dict.values():
#             if string == item:
#                 results.append(string)
#     return results


# print(ccommon_elements(my_dict))

# The Most pythonic way to solve is

def ccommon_elements(my_dict):
    return [key for key in my_dict.keys() if key in my_dict.values()]


print(ccommon_elements(my_dict))
