#펙토리아 계산기 : 1부터 n까지의 곱
#n = 5
#res = 1
#for i in range(1,n+1,1):
    #res = res * i
#print(res) #120



# 연습1
# 1000 - 2000 사이에서 홀수의 합을 구하는 프로그램
'''
hap = 0
for i in range(1001,2000,2):
    #print(i)
    hap = hap + i
print(hap)
'''

#실습2
#2단부터 9단까지 구구단

#for num1 in range(2,10,1): #단
    #for num2 in range(1,10,1): #곱하는 수
        #print(num1,'*',num2,'=\t',num1*num2)
        #pass


'''
while(True):
    num1 = int(input("숫자1===> "))
    num2 = int(input("숫자2===> "))
    if num1 == 0:
        break
    
    res = num1+num2
    print(num1,"+",num2,"=",res)
'''

'''res = 0
for i in range(1,101,1):
    if i%4 == 0:
        continue
    if i%3 == 0:
        continue
    res = res + i
print(res)
'''

