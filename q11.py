def my_fun():
    my_str=1/2+2/3+3/4+4/5
    my_list = list()
    for i in range(1,10):
        if i > 5:
            continue
        my_list.append(f'{i}/{i+1}')
    return my_list

print(my_fun())
