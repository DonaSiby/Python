def MinimumInteger(arr, num):
    sumArray = sum(arr)
    for element in sorted(arr):
        if sumArray <= num*element:
            return element
    print("No possible answer")


arr = [1, 1, 3, 2]
print(MinimumInteger(arr, len(arr)))
