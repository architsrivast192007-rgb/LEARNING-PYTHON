#Slicing in list
l1=[3,8,1,0,4,9,7,3,6]
print(l1[1:6:1])
#(it will not go to the 6th index which is "7")
print(l1[2:7:2])

#concatenation of lists
l1=[1,7,2]
l2=[0,5]
print(l1+l2)
print(l2+l1)

#Repetition of lists
print(l2*3)


#append()
#adds an item to the end of the list
fruits=["Mango","Apple","Orange"]
print(fruits)
#SYNTAX:-list.append(item)
fruits.append("Berries")
print(fruits)
print(fruits.append("Green apple"))

s1="python is fun"
print(s1.replace("python","c++"))


fruits.remove("Berries")
print(fruits)
fruits.remove("Green apple")
print(fruits)


#insert
#adds an element before specified index
#syntax: list.insert(index,item)
fruits.insert(0,"Juice")
print(fruits)
print(fruits.insert(3,"Green"))

#extend()
#remove()
#pop()

fruits=["Apple","Mango","Orange"]
print(fruits)
fruits.pop()
print(fruits)





