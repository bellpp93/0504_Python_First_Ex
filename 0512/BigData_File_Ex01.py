"""
    파이썬으로 빅데이터 파일 분석/처리
    년도별 출생아 수 통계처리하는 프로그램 작성
"""
def countBirths():
    ret = []  # list 자료구조 [(2008, 35253373),(2009, 635342626), ...]
    for y in range(2008, 2019):  # 2008년 ~ 2018년 까지
        count = 0
        filename = 'names/yob%d.txt' %y
        with open(filename, 'r') as f:  # f는 열린 파일 객체
            data = f.readlines()
            for d in data:
                if d[-1] == '\n':   # 한 줄의 데이터 마지막 끝이 엔터 '\n' 이면
                    d = d[:-1]      # Emma,F,18813 을 변수에 저장 => 슬라이싱을 적용하여 코딩
                birth = d.split(',')[2]
                count += int(birth)
        ret.append((y, count))      # append() 함수는 인자값 하나만 필요함!!
    return ret

result = countBirths()
with open('birth_by_year.csv', 'w') as f:  # f는 쓰기파일객체 => 읽기는 'r' 쓰기는 'w'
    print('-------------')
    print('년도별 출생아수')
    print('-------------')
    for year, birth in result:
        data = '%s,%s\n' %(year, birth)
        print(data)
        f.write(data)