# page 35
# 클래스 예시 만들어보기

class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized!")
    
    def hello(self):
        print("Hello, " + self.name + "!")
    
    def goodbye(self):
        print("Goodbye : " + self.name + "!")

m = Man("Minsu")
m.hello()
m.goodbye()
m.name
