my_list = list() #Create an empty list called my_list.

my_list.append(10) #Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(20) 
my_list.append(30)
my_list.append(40)
 
my_list.insert(len(my_list),15)#Insert the value 15 at the second position in the list.


list = [50,60,70]#Extend my_list with another list: [50, 60, 70].
my_list.extend(list)

my_list.remove(my_list[7])#Remove the last element from my_list.

my_list.sort()#Sort my_list in ascending order.

print(my_list[3])#Find and print the index of the value 30 in my_list

print(my_list)