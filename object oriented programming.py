class A():
    def __init__(self, rno):
        self.rno = rno
    def f1(self,name):
        return {self.rno, name}
class main():
    a1 = A(15)
    a2 = a1.f1("abc")
    print(a2)
main()
