"""
    리스트(list) 자료구조 실습 예제
"""
list1 = [10,20,30,40,50]
list2 = ['a','b','c']
list3 = [10,'a','abc',[10,20,30,40,50],['a','b','c']]
list1[0] = 60  # 리스트의 요소는 변경 가능
print(list1)  # [60, 20, 30, 40, 50]

def myfunc():
    print('Python Good!!')
list4 = [10,20,myfunc]
list4[2]()  # Python Good!!


"""
    튜플(tuple) 자료구조 실습 예제
"""
tuple1 = (10,20,30,40,50)
tuple2 = ('a','b','c')
tuple3 = (10,'a','abc',[10,20,30,40,50],['a','b','c'])
# tuple1[0] = 60  # 튜플의 요소는 변경 불가능
print(tuple1)  # (10, 20, 30, 40, 50)

def myfunc():
    print('Python Good!!')

tuple4 = (10,20,myfunc)
tuple4[2]()  # Python Good!!