def my_loop():
    j=0
    for i in range(10):
        if i==5:
            break
        j+=i
    return j

print(my_loop())