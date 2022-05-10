"""
    BMI(체질량지수) 계산하기를 파이썬 프로그램으로 작성
"""
weight = float(input("몸무게를 kg 단위로 입력하세요 >>> "))
height = float(input("키를 m 단위로 입력하세요 >>> "))

bmi = (weight/(height**2))

if bmi >= 20 and bmi <= 25:
    decision = "정상"
elif bmi >= 25.1 and bmi <= 29.9:
    decision = "과체중(1도 비만)"
elif bmi >= 30 and bmi <= 40:
    decision = "비만(2도 비만)"
elif bmi > 40.1:
    decision = "고도비만"
else:
    decision = "저체중"

print("당신의 BMI(체질량 지수) = ",bmi)
print("비만의 분류 = ",decision)