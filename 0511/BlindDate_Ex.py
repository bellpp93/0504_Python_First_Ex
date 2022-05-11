"""
    소개팅 커플 맺기 프로그램 작성
"""
from random import shuffle

male = ['김진홍','윤종인','홍지수','이형준','유동희']
female = ['성지영','김은정','김선정','이현아','이은진']

shuffle(male)
shuffle(female)
'''
zip() 함수는 각 리스트의 동일한 인덱스의 요소 끼리 묶는다.
결과는 튜플을 요소로 하는 리스트로 만들어 리턴하는 함수이다.
'''
couples = zip(male, female)  # zip() 함수는 list() 함수로 다시 변환을 해줘야 한다.
couples_data = list(couples)

for i, couple in enumerate(couples_data):
    print('커플%d : [%s]-[%s]' %(i+1, couple[0], couple[1]))