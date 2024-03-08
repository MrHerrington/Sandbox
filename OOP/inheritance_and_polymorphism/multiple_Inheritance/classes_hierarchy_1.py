class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(A):
    pass


class E(B, D):
    pass


# Test №1
print(issubclass(E, B))
print(issubclass(E, C))
print(issubclass(E, D))

# Test №2
print(issubclass(B, A))
print(issubclass(C, A))
print(issubclass(D, A))

# Test №3
print(A.mro())
print(B.__mro__)
print(C.mro())
print(D.__mro__)
print(E.mro())
