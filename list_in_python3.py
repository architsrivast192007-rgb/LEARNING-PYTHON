"""reverse()
sort()
count()
#Membership operation
"""
days_of_week = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
print(days_of_week)

# reverse()
days_of_week.reverse()
print(days_of_week)

# sort()
nums = [9, 0, 7, 5, 3]
print(nums)
nums.sort()
print("Sorted list is", nums)

#In descending order
nums.sort(reverse=True)
print(nums)

#count() "How many times a number occurred in a list"
numbers=[0,1,3,4,6,7,0,1,3,7,3]
print(f"the list is{numbers}")
item_to_count=int(input("Enter the number to be counted from the above list"))
c=numbers[item_to_count]
print(f"The counted list is {c}")

#in
l=["Python","Java","C++"]
print("Python" in l)
print("JavaScript" in l)
print("C++" not in l)
