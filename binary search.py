def binary_search(input_array, value):
    """Your code goes here."""
    min=0
    max=len(input_array)-1
    while max>=min:
        guess=int((min+max)/2)
        if input_array[guess]==value:
            return guess
        elif input_array[guess]<value:
            min=guess+1
        else:
            max=guess-1
    return -1
    
test_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
test_val1 = 61
test_val2 = 7
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
