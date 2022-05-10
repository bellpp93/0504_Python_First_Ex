"""
    'L'이라는 전자회사의 2022년 상반기 판매실적을
    천단위 마다 콤마 찍는 파이선 프로그램 작성
"""
# 자료구조 결정
sales_performance = {'1월':59870000, '2월':37650000, '3월':89425000}

# 최적화 소스
items = sales_performance.items()

print("<2022년 상반기 판매실적>")
for key, value in items:
    print(key + " 판매실적 :", format(value, ",") + "원")  # ",d"는 정수값의 3자리마다 컴마 찍기, d는 생략가능 => 형식지정자

# format(항목, "형식지정자")