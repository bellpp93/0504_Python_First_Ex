strdata = 'Time is money!!'
listdata = [1, 2, [1,2,3]]

print(strdata[5])  # [정답] i
print(strdata[-2])  # [정답] !
print(listdata[0])  # [정답] 1
print(listdata[-1])  # [정답] [1,2,3]
print(listdata[2][-1])  # [정답] 3

"""
문자열 자료 슬라이싱 => [시작인덱스:끝인덱스:스텝]
시작인덱스 '이상'부터 끝인덱스 '미만'까지 가져온다.
"""
print(strdata[1:5])  # [정답] ime(공백)
print(strdata[:7])  # [정답] Time is
print(strdata[9:])  # [정답] oney!!
print(strdata[:-3])  # [정답] Time is mone
print(strdata[-3:])  # [정답] y!!
print(strdata[:])  # [정답] Time is money!!
print(strdata[::2])  # [정답] Tm smny!