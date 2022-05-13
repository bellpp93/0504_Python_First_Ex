"""
    '년도별 인기 있는 상위 10개 이름을 통계처리' 하는 프로그램 작성
"""
from os.path import exists

def getTop10BabyName(year):
    # 자료구조
    nameMale = {}  # dictionary
    nameFemale = {}

    filename = 'names/yob%s.txt' %year  # ''로 묶였으니 문자열 => 숫자를 문자로 해야하기 때문에 %s 사용
    if not exists(filename):
        print('[%s] 파일이 존재하지 않습니다.' %filename)
        return None

    with open(filename, 'r') as f:  # with open => 파일을 열고 닫고 다 한다.
        data = f.readlines()
        for d in data:  # d 변수에는 Emma,F,20455(엔터(\n))이 저장
            if d[-1] == '\n':
                d = d[:-1]

            temp = d.split(',')
            name = temp[0]
            gender = temp[1]
            birth = temp[2]

            if gender == 'M':
                ret = nameMale  # nameMale이 dictionary이기 때문에 ret도 dictionary가 된다.
            else:
                ret = nameFemale

            if name in ret:
                ret[name] += int(birth)
            else:
                ret[name] = int(birth)

    retM = sorted(nameMale.items(), key=lambda x:x[1], reverse=True)
    retF = sorted(nameFemale.items(), key=lambda x:x[1], reverse=True)

    for i, name in enumerate(retM):  # 인덱스는 i가 받고, 실제값은 name이 받는다.
        if i > 9:
            break
        print('Top_%d 남자아이 이름 :%s' %(i+1, name))

    for i, name in enumerate(retF):
        if i > 9:
            break
        print('Top_%d 여자아이 이름 :%s' %(i+1, name))

y = input("인기순 상위 10개 이름을 알고 싶은 출생년도를 입력하세요 >>> ")
getTop10BabyName(y)