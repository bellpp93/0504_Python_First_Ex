"""
    게임 횟수를 입력받아 로또번호 자동 발생기를 파이썬 프로그램으로 작성(최적화 코딩)
"""
from random import shuffle
from time import sleep

game_num = int(input('로또 게임 횟수를 입력하세요 >>> '))

list_data = list(range(1, 46))

for i in range(1, game_num+1):
    shuffle(list_data)
    print('로또번호[%d] :' %i, sorted(list_data[:6]))
    sleep(1)