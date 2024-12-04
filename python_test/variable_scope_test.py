"""
Python variable scope
Keyword: scope, global, nonlocal, local, locals, globals
전역변수 : 주로 변하지 않는 상수 값, 전역적으로 사용되는 값
지역변수 : 함수 내의 로직 해결에 국한, 소멸주기 - 함수실행 종료시 소멸
전역변수를 지역내에서 수정하는 것은 권장하지 않음
"""

# Ex1
a = 10  # global variable


def foo():
    # Read global variable
    print("Ex1 >", a)


foo()

# Read global variable
print("Ex1 >", a)

print()
print()

# Ex2
b = 20  # global variable


def bar():
    b = 30  # local variable
    print("Ex2 >", b)  # Read local variable


bar()

print("Ex2 >", b)  # Read global variable

print()
print()

# Ex3
c = 40  # global variable


def foobar():
    # 글로벌 변수 수정 불가 (UnboundLocalError: local variable 'c' referenced before assignment)
    # c += 10
    # c = c + 10
    print("Ex3 >", c)


foobar()

print()
print()

# Ex4
d = 50  # global variable


def barfoo():
    # global 키워드를 사용하면 글로벌 변수 수정 가능
    global d
    d = 60
    d += 100
    print("Ex4 >", d)


barfoo()

print("Ex4 >", d)

print()
print()


# Ex5
def outer():
    e = 70  # outer function variable

    def inner():
        # e += 10 # UnboundLocalError: local variable 'e' referenced before assignment
        nonlocal e
        e += 10
        print("Ex5 >", e)

    return inner


in_test = outer()  # closure

in_test()
in_test()
in_test()

print()
print()


# Ex6
def func(var):
    x = 10  # local variable

    def printer():
        print("Ex6 >", "Printer Func inner", var)

    print("Func inner", locals())


func("Hi")

print()
print()

# Ex7
print("Ex7 >", globals())
print("a in globals() :", "a" in globals())
print("b in globals() :", "b" in globals())
print("c in globals() :", "c" in globals())
print("foo in globals() :", "foo" in globals())

print()
print()

# Ex8
for i in range(1, 10):
    for j in range(1, 10):
        globals()["mul_{}_{}".format(i, j)] = i * j

print("Ex8 >", mul_1_1)
print("Ex8 >", mul_5_5)
print("Ex8 >", mul_9_9)
print("mul_1_1 in globals() :", "mul_1_1" in globals())
print("mul_5_5 in globals() :", "mul_5_5" in globals())
print("mul_9_9 in globals() :", "mul_9_9" in globals())
