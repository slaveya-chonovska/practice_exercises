def check_if_same(lst1,lst2):
    return (len(lst1) == len(lst2)) and (sorted(str(lst2)) == sorted(str(lst1)))

print(check_if_same([1,2,3,4,"a"],[2,1,3,"a",4]))