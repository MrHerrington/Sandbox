class MROHelper:
    """Method Resolution Order(MRO) helper"""

    @staticmethod
    def len(cls):
        return len(cls.mro())

    @staticmethod
    def class_by_index(cls, n=0):
        return cls.mro()[n]

    @staticmethod
    def index_by_class(child, parent):
        return child.mro().index(parent)


# Test №1
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(MROHelper.len(D))
print(MROHelper.class_by_index(D, 2))
print(MROHelper.class_by_index(B))
print(MROHelper.index_by_class(D, A))
