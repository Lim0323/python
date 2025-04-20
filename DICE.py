import random

count = 0
dice1 = 0
dice2 = 0
dice3 = 0

dice1=random.randint(1,6)
dice2=random.randint(1,6)
dice3=random.randint(1,6)

while(True):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice3=random.randint(1,6)
    count = count + 1
    print(dice1,dice2,dice3)
    if ((dice1 == dice2) and (dice1 == dice3)):
            break

print("3개 주사위의 눈은 모두",dice1,"입니다.")
print("같은 숫자가 나오기까지",count,"번 던졌습니다.")

