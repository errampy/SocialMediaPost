def my_fun():
    list_obj = ['python','numpy']
    list_obj.insert(10,'NPL')
    return list_obj

print(my_fun())

#
'''
1. IndexError
2. None
3. ['NPL','python','numpy']
4. ['python','numpy','NPL]
'''
