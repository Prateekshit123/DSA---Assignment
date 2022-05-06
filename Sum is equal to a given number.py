def findPair(arr, n, sum):
    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] == sum):
                print("(", arr[i],
                      ", ", arr[j],
                      ")", sep = "")

arr = [5, 3, 8, 1, 7, 2]
n = len(arr)
sum = 6
findPair(arr, n, sum)