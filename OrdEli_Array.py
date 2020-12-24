def Sort_Array(arr):
    longitud=len(arr)
    for i in range(longitud-1):
        for x in range(longitud-1-i):
            if arr[x]>arr[x+1]:## Intercambia los valores del elemento en el que nos encontramos y el elemento siguiente, si el elemento en el que nos encontramos es mayor al siguiente.
                arr[x],arr[x+1]=arr[x+1],arr[x]
    return arr

def EliminateDuplicates(arr):
    longitud=len(arr)
    myarr=[]
    Sort_Array(arr)
    for i in range(longitud-1):
        if arr[i]!=arr[i+1]:## Elimina los elementos duplicados apartir de comprobar que se haya visto un elemento diferente.
            myarr.append(arr[i])
    myarr.append(arr[longitud-1])
    return myarr