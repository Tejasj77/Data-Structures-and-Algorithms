fibo_number = int(input())
def gen_fib(n):
    if n<=1:
        result = 1
        return result
    else:
        result = (gen_fib(n-1) + gen_fib(n-2))
    return result
output_list = []
for iter in range(fibo_number):
    output_list.append(gen_fib(iter))
print(output_list)