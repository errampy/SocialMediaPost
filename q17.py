def my_fun(a=None,b=None):
    my_list=list()
    for i in range(a,b):
        my_list.append(i)
    return my_list
print(my_fun(b=10,a=5))