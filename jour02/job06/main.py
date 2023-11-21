for i in range(2,1001):
    for k in range(2,i):
        if i % k == 0:
            break
    else:
        print(i)    