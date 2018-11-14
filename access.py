a = input("enter your username ")
if a == "sandeep" or a == "bhadra":
    print("Hi," + a + ": Enter your password")
    b = input()
    if b == "password":
        print("Access granted")
else:
    print( a +   " username is wrong, please enter a right user name to login")