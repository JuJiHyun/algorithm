def insertSort(A):
    for i in range(1, len(A)):
        for j in range(0, i):
            if A[i] < A[j]:
                small = j
                break
            else:
                small = i

        if small != i:
            a = A[i]
            for k in range(i, small, -1):
                A[k] = A[k-1]
                A[k-1] = A[k-2]
            A[small] = a

A = [22, 55, 44, 66, 11, 77, 99, 33, 88]
insertSort(A)
print(A)