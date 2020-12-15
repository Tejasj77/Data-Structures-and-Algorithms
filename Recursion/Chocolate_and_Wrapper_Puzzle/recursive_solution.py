def returnwrap(choco,wrap):
    if choco<wrap:
        return 0
    newChoco = choco/wrap
    return newChoco + returnwrap(newChoco + choco%wrap,wrap)

def chocoinput(money,price,wrap):
    if(money<price):
        return 0
    chocolates = money/price
    return int(chocolates + returnwrap(chocolates,wrap))

m,p,w = 15,1,3
print(chocoinput(m,p,w))