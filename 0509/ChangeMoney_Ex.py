"""
    금액을 입력받아 각 화폐 단위로 출력하는 파이썬 프로그램 작성
"""
money = int(input("금액을 입력해 주세요 >>> "))

list_money = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]
list_str_money = ["오만원권","만원권","오천원권","천원권","오백원","백원","오십원","십원","일원"]

for i in range(0,9):
    portion, remainder = divmod(money, list_money[i])
    money = remainder

    if portion > 0 and i < 4:
        print(list_str_money[i] + ' ' + str(portion) + '매')
    elif portion > 0 and i >= 4:
        print(list_str_money[i] + ' ' + str(portion) + '개')

# divmod는 몫과 나머지 값을 한번에 구하는 내장함수(built in 함수)이다. portion은 몫, remainder는 나머지 값.

'''
money, c50000, c10000, c5000, c1000, c500, c100, c50, c10 = 0,0,0,0,0,0,0,0,0
money = int(input("금액을 입력하세요 >>> "))

c50000 = money // 50000
money %= 50000
c10000 = money // 10000
money %= 10000
c5000 = money // 5000
money %= 5000
c1000 = money // 1000
money %= 1000
c500 = money // 500
money %= 500
c100 = money // 100
money %= 100
c50 = money // 50
money %= 50
c10 = money // 10
money %= 10

print("50000원 : %d매" %c50000)
print("10000원 : %d매" %c10000)
print("5000원 : %d매" %c5000)
print("1000원 : %d매" %c1000)
print("500원 : %d개" %c500)
print("100원 : %d개" %c100)
print("50원 : %d개" %c50)
print("10원 : %d개" %c10)
'''