def remove_every_other(my_list):
    return [value for index, value in enumerate(my_list) if not index % 2]


print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))