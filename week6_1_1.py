import turtle
# 이름을 입력 받아 변수에 저장
t = turtle.Turtle()
t.shape("turtle")
name = turtle.textinput("이름","이름을 입력하시오: ")

# 사각형 모양을 그리기
t.left(90)
t.forward(50)
t.write("안녕하세요" + name + "씨, 터틀 인사드립니다.")
t.forward(50)
t.left(90)
t.forward(50)
t.write("안녕하세요" + name + "씨, 터틀 인사드립니다.")
t.forward(50)
t.left(90)
t.forward(50)
t.write("안녕하세요" + name + "씨, 터틀 인사드립니다.")
t.forward(50)
t.left(90)
t.forward(50)
t.write("안녕하세요" + name + "씨, 터틀 인사드립니다.")
t.forward(50)
