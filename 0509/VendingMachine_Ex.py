"""
    파이썬으로 자동판매기 프로그램 작성
"""
money = int(input("투입된 돈 :"))
price = int(input("상품 값 :"))

change = money - price
print("거스름 돈 :",change)

coin500s = change // 500
change = change % 500
coin100s = change // 100

print("500원 동전의 개수 :",coin500s)
print("100원 동전의 개수 :",coin100s)