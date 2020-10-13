my_list = [4.5, None, -56, 'Привет', True, 15]


def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return


my_type(my_list)
