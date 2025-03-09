# #create a simple dictionary with empty and print
# dictionary = {}
# print(dictionary)

# ##create a dictionary 
# dictionary = {
#   "user1":"mohan" , 
#   "user2": "vasu" , 
# }
# print(dictionary)

# ##using clear method in dictionary
# dictionary_1 = {
#     "user1":"mohan" , 
#     "user2": "vasu" , 
# }
# dictionary_1.clear()
# print(dictionary_1)

# ##using copy method in dictionary
# dictionary_2 = {
#     "username":"mohan" ,
#     "password":"123@123" 
# }
# obj = dictionary_2.copy()
# print(obj)

# ## using get method in dictionary
# names = {
#     "1":"mohan" , 
#     "2":"srinu" ,
#     "3":"latha" ,
#     "4":"hima"
# }
# print(names.get("1"))

# ##using a square brakets
# names = {
#     "1":"mohan" , 
#     "2":"srinu" ,
#     "3":"latha" ,
#     "4":"hima"
# }
# print(names["4"])


# ##key method using the dictionary
# vegetables = {
#     "first":"tomatos" ,
#     "second":"onions" 
# }
# print(vegetables.keys())
# print(vegetables.values())

# ##dictionary using the item method
# vegetables = {
#     "first":"tomatos" ,
#     "second":"onions" 
# }
# print(vegetables.items())


# ##dictionary using the pop method
# shoes_types = {
#     1:"loafers",
#     2:"formals",
#     3:"running shoes"
# }
# shoes_types.pop(1)
# print(shoes_types)

# ##upadte method using dictionary
# prices = {
#     "rolex": "$2340" , 
#     "quartz":"$2349"
# }
# sample = {
#     "prince":"$2345", 
#     "jimmychoo":"$12345"
# }
# prices.update(sample)
# print(prices)

###removal of puctuation...........
puctuations = "!@$%^&*()_+[];:'',.<>?/"
my_str = input("enter the string :")
new_str = " "
for i in my_str :
    if i not in puctuations :
        new_str+=i
print(new_str)