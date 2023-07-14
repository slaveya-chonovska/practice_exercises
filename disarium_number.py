def disrium_number(n):
    i= len(str(n))
    if i == 1:
        return True
    digits_sum = 0
    og_num = n
    
    while n>0:
        digits_sum += (n%10)**i
        n = n//10
        i-=1

    return digits_sum == og_num

for num in range(1,201):
    if disrium_number(num):
        print("Disrium Number: ",num)