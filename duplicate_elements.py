#using collections
from collections import Counter

def find_duplicates_counter(lst):
    if len(lst) == len(set(lst)):
        return "No duplicates"
    lst_counter = Counter(lst)
    return tuple(i for i in set(lst) if lst_counter[i]>1)

#using dictionary
def find_duplicates(lst):
    if len(lst) == len(set(lst)):
        return "No duplicates"
    count_duplicates = {}
    for element in lst:
        if element not in count_duplicates:
            count_duplicates[element] = 1
        else: count_duplicates[element] +=1
    return tuple(k for k,v in count_duplicates.items() if v>1)

lst = [1,1,3,4,4,3,7,8,9,"a","d","a",3]
#print(find_duplicates(lst))
print(find_duplicates_counter(lst))