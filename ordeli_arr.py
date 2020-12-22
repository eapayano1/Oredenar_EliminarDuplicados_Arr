def Sort_Array(arr):
    longitud=len(arr)
    for i in range(longitud-1):
        for x in range(longitud-1-i):
            if arr[x]>arr[x+1]:##Si el elemento en el que nos encontramos es mayor al elemento siguiente entonces intercambiamos sus valores.
                arr[x],arr[x+1]=arr[x+1],arr[x]
    return arr

def EliminateDuplicate(arr):
    longitud=len(arr)
    myarr=[]
    Sort_Array(arr)
    for i in range(longitud-1):
        if arr[i]!=arr[i+1]:##Si el elemento en el que nos encontramos es diferente al elemento siguiente entonces guardamos el elemento en el que nos encontramos.
            myarr.append(arr[i])
    myarr.append(arr[longitud-1])

    return myarr