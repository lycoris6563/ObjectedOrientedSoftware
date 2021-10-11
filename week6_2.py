# 비어있는 리스트를 만든다.
friend_list = []
# 5명의 친구 이름을 입력 받는다
# 리스트에 추가한다.

name = input("친구 이름을 입력하시오")
friend_list.append(name)
name = input("친구 이름을 입력하시오")
friend_list.append(name)
name = input("친구 이름을 입력하시오")
friend_list.append(name)
name = input("친구 이름을 입력하시오")
friend_list.append(name)
name = input("친구 이름을 입력하시오")
friend_list.append(name)

# 리스트로 출력한다.
print(friend_list)

print("첫번째 친구 이름은",friend_list[0])
print("마지막 친구 이름은", friend_list[-1])
print("중간에 친구들 이름은",friend_list[1:4])

# 인덱스로 입력받기
index = int(input("인덱스 입력하기 1~5"))
# 해당 인덱스에 해당하는 친구 출력
print("해당 인덱스 %d 에 해당하는 친구 이름은" %index,friend_list[index-1])
