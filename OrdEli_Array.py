def Sort_Array(arr):
    longitud=len(arr)
    for i in range(longitud-1):
        for x in range(longitud-1-i):
            if arr[x]>arr[x+1]:## Intercambia los valores del elemento en el que nos encontramos y el elemento siguiente, si el elemento en el que nos encontramos es mayor al siguiente.
                arr[x],arr[x+1]=arr[x+1],arr[x]
    return arr