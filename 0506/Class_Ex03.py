class Add:  # 부모클래스
    def add(self, n1, n2):
        return n1 + n2

class Calculator(Add):  # 자식 클래스에서 '상속' 받는 법 => class 자식클래스명(부모클래스명):
    def sub(self, n1, n2):
        return n1 - n2

obj = Calculator()
print(obj.add(10, 20))  # 30
print(obj.sub(30, 10))  # 20