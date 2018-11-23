# Task1 - AIM

#1. Get 10 machines names
#2. Store them in a list
#3. Check weather (uat/prd) names falls under  manchines names list
#4. print the machines names list
#5. Finally find the length of the list




machines_names = []
for i in range(10):
  x = str(input("enter the machine names:  "))
  machines_names.insert(i,x)
  i+=1
print(machines_names)
if "uat" in machines_names:
  print("yes! UAT, it exits in machine names")
elif "prod" in machines_names:
  print("Yes PROD, exits in machines names" )
else:
  print("not in UAT and PROD")

print(machines_names)
print(len(machines_names))
print(machines_names[0])
#machines_names.append("sam")
#y = machines_names.copy()
#print(y)
#machines_names.count()
#z = [ ram, os ]
#machines_names.extend(z)
#machines_names.insert(2, centos)
#machines_names.reverse()
#machines_names.sort()
