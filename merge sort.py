def merge (input_arrray, p,q,r):
    lower_half=input_array[p:q+1]
    upper_half=input_array[q+1:r+1] 
    k,i,j=p,0,0
    while i<len(lower_half) and j<len(upper_half):
        if lower_half[i]<upper_half[j]:
            input_array[k]=lower_half[i]
            i+=1
        else:
            input_array[k]=upper_half[j]
            j+=1
        k+=1
    while i<len(lower_half):
        input_array[k]=lower_half[i]
        i+=1
        k+=1
    while j<len(upper_half):
        input_array[k]=upper_half[j]
        j+=1 
        k+=1        
def merge_sort(input_array,p,r):
    if r>p:
        q=(p+r)//2      
        merge_sort(input_array,p,q) 
        merge_sort(input_array,q+1,r)
        merge(input_array,p,q,r)
        
input_array = [14, 7, 3, 12, 9, 11, 6, 2,]
merge_sort(input_array, 0, len(input_array)-1)
print("Array after sorting: ",  input_array)    
