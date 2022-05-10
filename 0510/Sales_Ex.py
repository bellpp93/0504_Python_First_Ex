"""
    'L'이라는 전자회사의 2022년 상반기 판매실적을
    천단위 마다 콤마 찍는 파이선 프로그램 작성
"""
# 자료구조 결정
sales_performance = {'1월':59870000, '2월':37650000, '3월':89425000}
key_values = sales_performance.keys()
'''
        print(key_values)  # dict_keys(['1월', '2월', '3월'])
    판매금액에 천단위 마다 꼼마 찍기 => 59870000 => 59,870,000 변환
    알고리즘 및 로직(logic) 구상(시나리오) => 제어문의 조합 => for문, if문 활용
    시나리오를 순서있게 작성 => 우리말
    1. 59870000 => 00007895
    2. [0]
        00007895 => 8자리
        => 어떤 조건일 때 콤마를 넣을 건지? index값이 3의 배수이고 index값이 8자리하고 같지 않으면
                                        3자리 뒤에 콤마를 넣는다. => 000,078,95
    3. 000,078,95 => 59,870,000
'''
for keys in key_values:
    num = str(sales_performance[keys])
    value = num[::-1]  # "00007895"
    ret = ''
    for i, c in enumerate(value):

'''
[참고]
a = 4654321000
b = '{0:,}'.format(a)
print(b)  # 4,654,321,000

# for 반복문을 이용해서 문자열 뒤집기
name = "BlockDMask"
reverse_name = ''
for c in name:
    reverse_name = c + reverse_name
print(f'name : {name}')
print(f'reverse : {reverse_name}')
'''
