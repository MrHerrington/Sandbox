def parse_ranges(datas):
    splited_datas = (i for i in datas.split(','))
    result = (j
              for i in splited_datas
              for j in range(int(i.split('-')[0]), int(i.split('-')[-1]) + 1))
    return result


print(*parse_ranges('1-2,4-4,8-10'))
print(*parse_ranges('1-10,2-10'))
print(*parse_ranges('7-32'))
