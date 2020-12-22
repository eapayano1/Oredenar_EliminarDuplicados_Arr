def Sort_Array(arr):
    n=len(arr)
    for i in range(n-1):
        for x in range(n-1-i):
            if arr[x]>arr[x+1]:
                arr[x],arr[x+1]=arr[x+1],arr[x]
    return arr