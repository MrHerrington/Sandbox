import pickle


def filter_dump(file_name, no_serialize_lst, types):
    with open(file_name, mode='wb') as file:
        new_lst = []
        for i in no_serialize_lst:
            if type(i) is types:
                new_lst.append(i)
        pickle.dump(new_lst, file)
        return new_lst


print(filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int))
