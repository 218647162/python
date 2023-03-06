#Student Name:Evance Masuku
#Student no:218647162
#Date:Mar 2023
#Assignment 3:Python

#Given the String:
s="fullstackslp"

#"f"
print(s[0])

#"p"
print(s[11])

#"stack"
print(s[4:9])

#"slp"
print(s[9:])

#"cks"
print(s[7:10])

#Bones: Use indexxing to reverse the string
#fullstackslp = plskcatslluf
print(s[:0])

########################
#Probelm 2

d1={'simple_key':'hello'}
print(d1['simple_key'])

d2={'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3={'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

 
###########################################
#problem 4

mylist=[1,1,1,1,1,2,2,2,2,3,3,3,3]
new_set = set(mylist)
print(new_set)


#Probelem 5
age=45
name="kyle"

print("hello my dog's name is {} and he looks {} years old".format(name,age))