# Brute force solution

def twoSumBruteForce(arr, target):
    for i in range(len(arr)):
        numToFind = target - arr[i]
        for j in range(i + 1, len(arr)):
            if(arr[j] == numToFind):
                print("INDEXES: " + str([i, j]))
                print("VALUES: " + str([arr[i], arr[j]]))
                return
    return False


twoSumBruteForce([1, 2, 3, 4, 5], 6)
