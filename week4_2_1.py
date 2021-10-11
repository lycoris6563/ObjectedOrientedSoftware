# 커피 가게 매출 계산기

# 아메리카노 2000원
# 카페라떼 3000원
# 카푸치노 3500원

am = int(input("아메리카노 판매 개수:"))
cl = int(input("카페라떼 판매 개수:"))
cc = int(input("카푸치노 판매 개수:"))

total = am * 2000 + cl * 3000 + cc * 3500
ingrd = 100000

gain = total - ingrd

print("총매출은",total,"원 입니다")
print("순이익은",gain,"원 입니다")
