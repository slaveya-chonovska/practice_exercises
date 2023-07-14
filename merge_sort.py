def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        left_array = arr[:mid]
        right_array = arr[mid:]

        merge_sort(left_array)
        merge_sort(right_array)

        i = j = k = 0 #index for the left, right, merged subarray

        while i<len(left_array) and j<len(right_array):
            if left_array[i] <= right_array[j]: #here the sign determines the sorting order
                arr[k] = left_array[i]
                i+=1
            else:
                arr[k] = right_array[j]
                j+=1
            k+=1

        #if there are any leftover elements in the left subarray
        while i<len(left_array):
            arr[k] = left_array[i]
            k+=1
            i+=1

        #if there are any leftover elements in the right subarray
        while j<len(right_array):
            arr[k] = right_array[j]
            k+=1
            j+=1




a = [4,8,4,8,1,2,5]
merge_sort(a)

print(a)