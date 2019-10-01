def bubbleSort(list):
    for i in range(len(list)):
        for i in range(len(list)-i-1):
            if list[i] > list[i+1]:
                temp = list[i+1]
                list[i+1] = list[i]
                list[i] = temp
    return(list) 

A = [44, 22, 33, 55, 88, 77, 11, 66]
print(bubbleSort(A))