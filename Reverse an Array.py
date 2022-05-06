def revArray(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1

A = [1, 3, 4, 6, 3, 2]
print(A)
revArray(A, 0, 5)
print("Reversed list is: ", A)