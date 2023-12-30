            ############# Question no 1 #############

#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

sample_list=[(2,5),(1,2),(4,4),(2,3),(2,1)]
print("Orignal List : ",sample_list)

lst1=[]
lst2=[]
for a,b in sample_list:
  lst1.append((b,a))
  lst1.sort()
for a1,b1 in lst1:
  lst2.append((b1,a1))
print("Sorted List : ",lst2)
