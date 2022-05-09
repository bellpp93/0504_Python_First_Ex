# 파이썬 자료구조
# List
list1 = [1,2,3]
print(type(list1))  # <class 'list'> 출력
print(list1)  # [1, 2, 3] 출력
print(list1[0])  # 1 출력
print(list1[2])  # 3 출력

# Tuple
tuple1 = (1,2,3)
print(type(tuple1))  # <class 'tuple'>
print(tuple1)  # (1, 2, 3)
print(tuple1[0])  # 1

# Set
set1 = set([1,2,3])
print(type(set1))  # <class 'set'>
print(set1)  # {1, 2, 3}

set2 = {1,2,3}
print(type(set2))  # <class 'set'>
print(set2)  # {1, 2, 3}

# Dictionary
dict1 = {'name':'손흥민','phone':'010-5421-1111','email':'son77@naver.com'}
print(type(dict1))  # <class 'dict'>
print(dict1['name'])  # 손흥민 => 키 값('name')을 준다.
print(dict1['phone'])  # 010-5421-1111
print(dict1['email'])  # son77@naver.com
print(dict1)  # {'name': '손흥민', 'phone': '010-5421-1111', 'email': 'son77@naver.com'}

string1 = "Python is Good!"
print(type(string1))  # <class 'str'>
