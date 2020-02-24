
def bubble_sort(arr):
    if len(arr) <= 1:
        print(arr)
    
    for i in range(len(arr)-1,0,-1):
        for j in range(0,len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print(arr)
