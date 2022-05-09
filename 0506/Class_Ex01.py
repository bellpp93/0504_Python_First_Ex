class MyClass:
    var = '안녕하세요'  # 클래스 멤버

    def sayHello(self):  # 클래스 메소드
        print(self.var)  # 안녕하세요

obj = MyClass()  # obj는 객체참조변수, MyClass 인스턴스 객체 생성
print(obj.var)  # 안녕하세요
obj.sayHello()
