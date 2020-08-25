nums1 = [1,2,3,4]
nums2 = [3,4,5,6]
answer = [num for num in nums1 if num in nums2]
print(f"answer is {answer}")

names = ["Elie", "Tim", "Matt"]
answer2 = [x[::-1].lower() for x in names]
print(f"answer2 is {answer2}")

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = artist["first"] + " " + artist["last"]
print(f"Full Name = {full_name}")

from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:

# if food in bakery_stock:
#     print(str(bakery_stock[food]) + " left")
# else:
#     print("We don't make that")
if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("We don't make that")