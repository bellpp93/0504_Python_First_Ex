"""
    게임 횟수를 입력받아 로또번호 자동 발생기를 파이썬 프로그램으로 작성
"""
from random import shuffle
from time import sleep

game_num = input('로또 게임 횟수를 입력하세요 >>> ')

for i in range(int(game_num)):  # 0 ~ 4
    balls = list(range(1,46))   # 1 ~ 45 까지 만들겠다.
    lotto_result = []           # 데이터가 없는 빈 리스트 자료구조 생성

    for j in range(6):          # 0 ~ 5 즉, 6번 반복해라
        shuffle(balls)          # 1 ~ 45 까지를 무작위로 섞는다.
        number = balls.pop()
        lotto_result.append(number)
    lotto_result.sort()         # 오름차순으로 정렬시켜라
    print('로또번호[%d] :' %(i+1), end=' ')
    print(lotto_result)
    sleep(1)  # cpu시간을 조절하는 것이 'sleep'