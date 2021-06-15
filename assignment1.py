lst = []
chem =input("Enter chemistry marks out of 100")
chem = int(chem)
lst.append(chem)
maths = input("Enter maths marks out of 100")
maths = int(maths)
lst.append(maths)
physics = input("Enter physics marks out off 100")
physics = int(physics)
lst.append(physics)
english = input("Enter english marks out of 100")
english = int(english)
lst.append(english)
print ("Marks you entered are in sequence of: chemistry,maths,physics,english")
a = sum(lst)
percentage = a/4
print ("The percentages the student have is : ",percentage,"%")
if percentages>70:
    print ("Grade A")
else:
    print ("Grade B")    


