inp_number = int(input())

def gen_fib(n):
    if n<=1:
        return 1
    bottom_top = [None]*(inp_number+1)
    bottom_top[0] = 1
    bottom_top[1] = 1
    for iter in range(2,n+1):
        bottom_top[iter] = bottom_top[iter-1] + bottom_top[iter-2]
    return bottom_top

print(gen_fib(inp_number))
