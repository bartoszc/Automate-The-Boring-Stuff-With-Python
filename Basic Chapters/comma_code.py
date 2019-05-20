def conv(old_list):
    new_str = ""
    new_list = old_list[0:-1]
    last = old_list[-1]
    for i in new_list:
        a = str(i)
        new_str += a + ", "
    new_str += "and " + str(last)
    print(new_str)


conv(['apples', 'bananas', 'tofu', 'cats', 'dogs'])

#########################################################################

spam = ['apples', 'pizza', 'dogs', 'cats']


def comma(items):
    for i in range(len(items) - 2):
        print(items[i] + ', ', end="")
    print(items[-2] + ' and ' + items[-1])


comma(spam)
