
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3 and num2 >= num1:
        return num2
    else:
        return num3

x = input("enter first number:  ")
y = input("enter the second number: ")
z = input("enter the third number: ")
print(max_num(x, y, z))