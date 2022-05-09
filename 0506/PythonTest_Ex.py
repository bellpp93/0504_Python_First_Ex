strdata = 'Time is money!!'
listdata = [1, 2, [1,2,3]]

print(strdata[5])  # [정답] i
print(strdata[-2])  # [정답] !
print(listdata[0])  # [정답] 1
print(listdata[-1])  # [정답] [1,2,3]
print(listdata[2][-1])  # [정답] 3

""" 문자열 자료 슬라이싱 => [시작인덱스:끝인덱스:스텝]
시작인덱스 '이상'부터 끝인덱스 '미만'까지 가져온다. """

print(strdata[1:5])  # [정답] ime(공백)
print(strdata[:7])  # [정답] Time is
print(strdata[9:])  # [정답] oney!!
print(strdata[:-3])  # [정답] Time is mone
print(strdata[-3:])  # [정답] y!!
print(strdata[:])  # [정답] Time is money!!
print(strdata[::2])  # [정답] Tm smny!

# 정보처리 실기 기출문제 풀이1
country = {'한국', '미국', '프랑스', '일본'}  # 집합변수
country.add('영국')
country.add('싱가폴')
country.remove('일본')
country.update(['홍콩', '한국', '스위스'])  # 여러개를 추가하는 개념
print(country)
# [정답] - 파이썬 자료구조의 Set은 '순서를 유지하지 않고 저장', '중복을 허용하지 않음'
# {'스위스', '영국', '싱가폴', '미국', '한국', '홍콩', '프랑스'}
# {'영국', '한국', '홍콩', '싱가폴', '스위스', '프랑스', '미국'}

# 정보처리 실기 기출문제 풀이2
class good:
    li = ["seoul", "kyeonggi", "inchon", "daejeon", "daegu", "pusan"]
g = good()  # good 인스턴스 객체 생성
str01 = ''  # 빈 문자열

for i in g.li:
    str01 = str01 + i[0]
print(str01)
# [정답] - 처음에 for문 i에 seoul => i[0]은 첫번째 문자인 s를 가져온다. 같은 원리로 반복
# skiddp

# 정보처리 실기 기출문제 풀이3
lol = [[1,2,3],[4,5],[6,7,8,9]]
print(lol[0])
print(lol[2][1])

for sub in lol:
    for item in sub:
        print(item, end='')
    print()  # 줄바꿈
# [정답]
# [1,2,3]
# 7
# 123
# 45
# 6789

# 정보처리 실기 기출문제 풀이4
li = ['Korea', 'America', 'China']
a = 0
str01 = ''

for i in li:
    for j in i:
        str01 += j[0]
        a = a+1
        if a > 5:
            break
print('a:',a,'str01:',str01)
# [정답]
# a: 7 str01: KoreaAC

# 정보처리 실기 기출문제 풀이5
a, b = 100, 200
print(a == b)
# [정답] False => 첫 글자는 대문자로 함.

# 정보처리 실기 기출문제 풀이6
a = 100
resulr = 0

for i in range(1,3):  # 1부터 3미만까지 => 즉 1,2
    result = a >> i  # >> 비트(0 또는 1) 연산자
    result = result + 1
print(result)
# [정답] 26