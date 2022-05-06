sales = {'1월':95, '2월':100, '3월':130, '4월':90, '5월':150, '6월':170}
iterable_data = sales.items()
print(iterable_data)

for item in iterable_data:
    print(item)

"""
items()메소드는 
사전(dict)의 모든 '키:값'을 추출하여 반복 가능한 자료인 dict_items 사전 뷰 객체로 리턴
"""