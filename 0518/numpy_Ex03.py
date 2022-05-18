"""
    파이썬 numpy 라이브러리를 활용하여 행렬의 곱(dot product) 처리하기
    [문제 2]
    'oo 전자'는 세 종류의 제품 A,B,C를 한국과 미국 시장에 판매하고 있다.
    'oo 전자'가 올해에 각 시장에서 판매한 양은 다음과 같다.

    제품 A : (한국) 5000 (미국) 2000
    제품 B : (한국) 2000 (미국) 3000
    제품 C : (한국) 1500 (미국) 1000

    또한 제품 A,B,C의 단위당 가격은 다음과 같다. (단위 : 백만원)
    제품 A : 2
    제품 B : 4
    제품 C : 3

    그리고 제품별 단위당 원가는 다음과 같다. (단위 : 백만원)
    제품 A : 1.8
    제품 B : 3.5
    제품 C : 2.5

    위 데이터를 참고하여 행렬을 만들고 numpy 패키지를 이용하여
    행렬의 곱 연산을 취한 후 '지역별 매출액', '지역별 원가', '지역별 이익'을 산출하세요.
"""
import numpy as np

# 지역 행렬
R = np.array([[5000,2000,1500],
              [2000,3000,1000]])

# 가격 행렬
P = np.array([[2],
              [4],
              [3]])

# 원가 행렬
CP = np.array([[1.8],
               [3.5],
               [2.5]])

RP = np.dot(R,P)
RCP = np.dot(R,CP)
RP_RCP = RP - RCP

print("한국과 미국의 지역별 매출액\n", RP)
flatten_list1 = RP.flatten()  # flatten() 함수는 다차원 배열을 1차원 배열로 바꾸어 준다.
annual_sales = sum(flatten_list1)
print("* 지역별 연간 매출액 >>> ", annual_sales, '\n')

print("한국과 미국의 지역별 원가\n", RCP)
flatten_list2 = RCP.flatten()
total_costs = sum(flatten_list2)
print("* 지역별 연간 총원가 >>> ", total_costs, '\n')

print("한국과 미국의 지역별 이익\n", RP_RCP)
flatten_list3 = RP_RCP.flatten()
gross_margin = sum(flatten_list3)
print("* 지역별 연간 총이익 >>> ", gross_margin)

# <실행결과>
# 한국과 미국의 지역별 매출액
#  [[22500]
#  [19000]]
# * 지역별 연간 매출액 >>>  41500
#
# 한국과 미국의 지역별 원가
#  [[19750.]
#  [16600.]]
# * 지역별 연간 총원가 >>>  36350.0
#
# 한국과 미국의 지역별 이익
#  [[2750.]
#  [2400.]]
# * 지역별 연간 총이익 >>>  5150.0