def partition(array,p,r):
    q,i=r,p           
    while q>0 and i<q:              
        while array[q]<array[i]:
            if i==q-1:
                array[i],array[q] =array[q], array[i]
            else:
                array[q-1],array[q],array[i]=array[q],array[i],array[q-1]
            q-=1               
        i+=1
    return q

def quicksort(array,p,r):        
    if r>p:
        pivot=partition(array,p,r)
        quicksort(array,p,pivot-1)
        quicksort(array,pivot+1,r)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
quicksort(test,0,len(test)-1)
print (test)
