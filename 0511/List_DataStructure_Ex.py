"""
    list 자료구조에서 새로운 객체 추가하기
"""
list_name = ['박태호','오수철','손유일','김종오']

list_name.append('이두희')

position = list_name.index('손유일')  # 2 => 0,1 다음에 2번에 위치
list_name.insert(position,'홍길동')  # insert는 인자값 2개
# list_name.append(position,'홍길동')  # 오류발생 append는 인자값 1개

print(list_name)