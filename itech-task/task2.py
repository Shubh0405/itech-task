def cal_series(a):
    for i in range(1,a+1):
        if(i%2 == 0):
            print((i*i)-1)
        else:
            print((i*i)+1)

cal_series(9)
