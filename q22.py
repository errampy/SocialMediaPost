def my_fun():
    my_list1 = ["a","b"]
    my_list2 = ['c','d']
    my_list1.extend(my_list2)
    return my_list1
print(my_fun())