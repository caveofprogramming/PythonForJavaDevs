class A:
    def run(self):
        print("Hello A")

class B:
    def run(self):
        print("Hello B")

class C(A, B):
    pass

c = C()
c.run()

print(C.mro())