class H:
    pass


class D(H):
    pass


class E(H):
    pass


class F(H):
    pass


class G(H):
    pass


class B(D, E):
    pass


class C(F, G):
    pass


class A(B, C):
    pass


# Test №1
print(issubclass(D, H))
print(issubclass(E, H))
print(issubclass(F, H))
print(issubclass(G, H))

# Test №2
print(issubclass(B, D))
print(issubclass(B, E))
print(issubclass(B, F))
print(issubclass(B, G))

# Test №3
print(issubclass(C, D))
print(issubclass(C, E))
print(issubclass(C, F))
print(issubclass(C, G))

# Test №4
print(H.mro())
print(G.mro())
print(F.mro())
print(E.mro())
print(D.mro())
print(C.mro())
print(B.mro())
print(A.mro())
