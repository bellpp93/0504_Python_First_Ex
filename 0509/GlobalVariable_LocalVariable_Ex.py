"""
    파이썬의 전역변수와 지역변수 실습 예제
"""
param = 10
strdata = '전역변수'  # 함수 밖에서 선언

def func1():
    strdata = '지역변수'  # 함수 안에서 선언
    print(strdata)

def func2(param):
    param = 1

def func3():
    global param
    param = 50

func1()  # [출력] 지역변수(함수 내에서만 유효)
print(strdata)  # [출력] 전역변수(코드 전반에 걸쳐 유효)

func2(param)
print(param)  # [출력] 10

func3()
print(param)  # [출력] 50


# 멤버 체크하기
listdata = [10,20,30,40]
result1 = 50 in listdata  # 값 in 자료구조
print(result1)  # [출력] False

result2 = 40 in listdata
print(result2)  # [출력] True