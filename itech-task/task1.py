def cal_func(x,n):

    sum = 0
    for i in range(1,n+1):
        sum += (1/(x)**i)

    return sum

def cal_func_using_recrusion(x,n):

    if n==1:
        return 1/x
    else:
        return 1/(x**n) + cal_func_using_recrusion(x,n-1)

print(cal_func(3,5))
print(cal_func_using_recrusion(3,5))
