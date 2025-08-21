def cumulative_prod(ls1):
    p = 1
    for i in ls1:
        p *= i
        print(p)


ls1 = [1,2,3,4,5]
print(cumulative_prod(ls1))
