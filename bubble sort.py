def bubble_sort(input_array):
    j=0
    while j<len(input_array)-1:
        i=0
        while i<len(input_array)-1:
            if input_array[i]>input_array[i+1]:
                swap=input_array[i]
                input_array[i]=input_array[i+1]
                input_array[i+1]=swap
            i+=1
        j+=1
    return input_array
input_array=[78, 49,28,-1,190,65,-8, 98]
print(bubble_sort(input_array))
