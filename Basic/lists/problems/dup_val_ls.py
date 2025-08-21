
ls = [1,2,23,32,331,3,4,5,331,23]

uni = []

for i in ls:
    if i in uni:
        continue
    else: uni.append(i)

print(uni)
