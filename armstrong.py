

def arm():
    reminder=0
    sum=0
    count=0

    num1=int(input("enter armstrong :"))
    copy=num1
    copy2=num1

    while copy2 > 0:
        copy2=copy2//10
        count+=1


    while copy > 0:
        reminder=copy%10
        sum=sum+(reminder**count)
        copy=copy//10

    if num1 == sum:
        print(f"{num1} is armstrong")
    else: 
        print(f"{num1} is not armstrong ")

arm()        