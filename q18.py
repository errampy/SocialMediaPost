def my_fun(a,b):
    c=a.count(b)
    my_list = list()
    for i in a:
        my_list.append(i//c)
    return set(my_list)

a = [10,20,10,20,30,40,50]
b = 10
print(my_fun(a,b))