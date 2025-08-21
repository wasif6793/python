
ls = [1,2,3,3,4,5,5,6,7,6,8,3]
ls2 = []

def find_dup_list(ls):
    flag = 0
    for i  in ls:
        cntrl = ls.count(i)
        if cntrl >= 1:
            flag = 1
            break
    if(flag == 1):
        print("There is duplicate element in the list")
    else:
        print("There is no duplicate element in the list")

find_dup_list(ls)
