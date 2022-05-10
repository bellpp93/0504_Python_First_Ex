"""
BMI를 구하는 함수를 정의
BMI를 구하는 공식 : height / (weight**2)
이 때 height의 단위는 cm, weight의 단위는 kg이다.
"""

def BMI_calc(a, b):
    return float(a/(b ** 2))

# 자신의 키와 몸무게를 입력하고

weight = float(input("몸무게를 kg 단위로 입력하세요 >>> "))
height = float(input("키를 cm 단위로 입력하세요 >>> "))
height_m = height / 100

BMI = BMI_calc(weight, height_m)

# BMI 결과에 따라 비만 유무를 판정한다.

if BMI >= 23 and BMI < 25 :
    BMI_result = "과체중(1도 비만)"
elif BMI >= 25 and BMI < 30 :
    BMI_result = "비만(2도 비만)"
elif BMI >= 30 :
    BMI_result = "고도비만"
else:
    BMI_result = "정상"

# 결과를 출력한다.

print("당신의 BMI는 %d 입니다." %BMI)
print("당신은 %s 입니다." %BMI_result)