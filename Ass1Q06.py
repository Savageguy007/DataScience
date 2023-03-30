def check(lst):
    lst1=[]
    set1=set(lst)
    for i in set1:
     if lst.count(i)>=2:
           lst1.append(i)
    print('MStringList1',lst1)
    print(list(set1))
lst=eval(input("Enter the list : "))
check(lst)