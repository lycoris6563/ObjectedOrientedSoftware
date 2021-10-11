#첫번째 사람
fName = input("첫번째 사람의 이름: ")
fAge = int(input("첫번째 사람의 나이: "))
fHeight = float(input("첫번째 사람의 키:"))

#두번째 사람
sName = input("두번째 사람의 이름: ")
sAge = int(input("두번째 사람의 나이: "))
sHeight = float(input("두번째 사람의 키:"))

#세번째 사람
tName = input("세번째 사람의 이름: ")
tAge = int(input("세번째 사람의 나이: "))
tHeight = float(input("세번째 사람의 키:"))

#키의 합
hPls = fHeight + sHeight + tHeight

#키의 평균
hAvg = hPls/3

#나이의 합
aPls = fAge + sAge + tAge

print("%s,%s,%s의 키의 합은 %f이고, 평균은 %f이며 나이의 합은 %d이다." % (fName, sName, tName, hPls, hAvg, aPls))
