def selectionSort(A, n):
    for i in range(len(A)):
        min = i
        for j in range(i+1, len(A)):
            if A[j] < A[min]:
                min = j
        temp = A[i]
        A[i] = A[min]
        A[min] = temp
    return A

A = [22, 44, 11, 66, 88, 11, 55, 99, 77]
b = selectionSort(A, 9)
print(b)