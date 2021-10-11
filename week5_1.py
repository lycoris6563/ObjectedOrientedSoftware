#투입한 돈을 입력
money = int(input("투입할 돈을 입력 하세요: "))

#물건값을 입력
price = int(input("물건 값을 입력 하세요:  "))

#거스름돈 계산 출력
change = money - price
print("거스름돈 = ",change)

#동전 계산
#500원 동전 수 계산

n500 = change // 500
change_rem = change % 500

#100원 동전 수 계산
n100 = change_rem // 100
change_rem %= 100

#50원 동전 수 계산
n50 = change_rem // 50
change_rem %= 50

#10원 동전 수 계산
n10 = change_rem //10

#각 동전수 출력
print("500원 동전 수 = ",n500)
print("100원 동전 수 = ",n100)
print("50원 동전 수 = ",n50)
print("10원 동전 수 = ",n10)
