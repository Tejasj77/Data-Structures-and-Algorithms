inp_number = int(input())
memo = [None]*inp_number
op = []

def gen_fib(n,memo):
    if memo[n]!=None:
        return memo[n]
    if n<=1:
        return 1
    else:
        result = (gen_fib(n-1,memo) + gen_fib(n-2,memo))
        memo[n] = result
    return result

for iter in range(inp_number):
    op.append(gen_fib(iter,memo))
print(op)