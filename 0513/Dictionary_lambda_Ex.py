names = {'박태호':85,'오수철':70,'손유일':90,'안재홍':65,'이두희':80}

ret1 = sorted(names)
# sorted() 함수에 dictionary를 인자값으로 주면 key를 오름차순으로 정렬한 결과를 리스트로 리턴해준다.
print(ret1)  # ['박태호', '손유일', '안재홍', '오수철', '이두희'] => 키만 추출

'''
def f1(x):
    return x[0]

def f2(x):
    return x[1]
'''

# ret2 = sorted(names.items(), key=f1)      # f1 '키'로 오름차순
# print(ret2)  # [('박태호', 85), ('손유일', 90), ('안재홍', 65), ('오수철', 70), ('이두희', 80)]

ret2 = sorted(names.items(),key=lambda x:x[0])
print(ret2)

# ret3 = sorted(names.items(), key=f2)      # f2 '값'으로 오름차순
# print(ret3)  # [('안재홍', 65), ('오수철', 70), ('이두희', 80), ('박태호', 85), ('손유일', 90)]

ret3 = sorted(names.items(), key=lambda x:x[1])
print(ret3)

# ret4 = sorted(names.items(), key=f2, reverse=True)        # f2 '값'으로 내림차순
# print(ret4)  # [('손유일', 90), ('박태호', 85), ('이두희', 80), ('오수철', 70), ('안재홍', 65)]

ret4 = sorted(names.items(), key=lambda x:x[1], reverse=True)
print(ret4)