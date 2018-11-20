
machines_names = []
for i in range(10):
  x = str(input("enter the machine names:  "))
  machines_names.insert(i,x)
  i+=1
# if "uat" in machines_names:
#  print("yes UAT, it exits in machine names    "+x )
#elif " prod" in machines_names:
#  print("Yes PROD, exits in machines names" )

print(machines_names)
print(len(machines_names))
