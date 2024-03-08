from collections import UserList


class CustomRange(UserList):
    def __init__(self, *args):
        super().__init__()
        new_lst = []
        new_lst.extend(args)
        temp_lst = []
        for i in new_lst:
            if isinstance(i, str):
                for j in range(int(i.split('-')[0]), int(i.split('-')[-1]) + 1):
                    temp_lst.append(j)
            else:
                temp_lst.append(i)
        self.data = temp_lst


# Test №1
customrange = CustomRange(1, '2-5', 5, '6-8')
print(customrange[0])
print(customrange[1])
print(customrange[2])
print(customrange[-1])
print(customrange[-2])
print(customrange[-3])

# Test №2
customrange = CustomRange(1, '2-5', 3, '1-4')
print(*customrange)
print(*reversed(customrange))
print(len(customrange))
print(1 in customrange)
print(10 in customrange)

# Test №3
customrange = CustomRange()
print(len(customrange))
print(*customrange)
print(*reversed(customrange))
