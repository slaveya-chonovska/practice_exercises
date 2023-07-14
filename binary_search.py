def binary_search(lst,x):
    lst = sorted(lst)

    l = 0
    r = len(lst) -1

    while l<=r:
        m = l + (r-l)//2
        if(x == lst[m]):
            return True
        if x<lst[m]:
            r = m - 1
        else:
            l = m + 1
    
    return False

print(binary_search([1,2,3,4,6,7],6))