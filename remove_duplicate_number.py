lst=[1,2,2,3,4,4,5,6,6]
uniqe_lst=[]
for i in lst:
    if i not in uniqe_lst:
        uniqe_lst.append(i)
print(uniqe_lst)