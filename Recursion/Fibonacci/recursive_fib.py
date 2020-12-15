end_count = int(input("Enter the ending point of the counter ?"))

def gen_fib(n):
    if n<=1:
        return n
    else:
        return (gen_fib(n-1)+gen_fib(n-2))
output_list = []
for i in range(end_count):
    output_list.append(gen_fib(i))
print(output_list)