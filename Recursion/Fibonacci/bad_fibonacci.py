#Fibonacci numbers is the array consisting of i elements where ith element is the sum of i-1 and i-2.

end_count = int(input("Index upto which fibonacci numbers are to be generated ?"))

def gen_fib(counter):
    iter=1
    if counter==0:
        fib = []
    elif counter==1:
        fib = [1]
    elif counter==2:
        fib = [1,1]

    else:
        fib = [1,1]
        while iter<counter-1:
            fib.append(fib[iter] + fib[iter-1])
            iter += 1
    return fib
print(gen_fib(end_count))
