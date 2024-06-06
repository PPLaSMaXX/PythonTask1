class A:
    say_text = 'baseclass'
    def say_something(self):
        print(self.say_text)

class B(A):
    say_text = 'Bob'

class P(A):
    say_text = 'Piter'

class C(A):
    say_text = 'Chloe'

class D(B,C):
    pass

class E(C,P,B):
    pass

class F(P):
    pass

b = B()
b.say_something()

p = P()
p.say_something()

c = C()
c.say_something()

d = D()
d.say_something()

e = E()
e.say_something()

f = F()
f.say_something()
