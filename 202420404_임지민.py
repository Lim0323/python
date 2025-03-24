num1 = input("숫자1 ==> ")
num1 = int(num1)

num2 = input("숫자2 ==> ")
num2 = int(num2)

addValue = num1 + num2
subValue = num1 - num2
mulValue = num1 * num2
divValue = num1 / num2
remainder = num1 % num2
squValue = num1 ** num2

print(num1,"+",num2,"=", addValue)
print(num1,"-",num2,"=", subValue)
print(num1,"*",num2,"=", mulValue)
print(num1,"/",num2,"=", divValue)
print(num1,"%",num2,"=", remainder)
print(num1,"**",num2,"=", squValue)