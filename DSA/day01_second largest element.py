class Solution:
    def getSecondLargest(self, arr):
        largest = -1
        secondLargest = -1

        for i in range(len(arr)):
            if arr[i] > largest:
                secondLargest = largest
                largest = arr[i]

            elif arr[i] < largest and arr[i] > secondLargest:
                secondLargest = arr[i]

        return secondLargest


obj = Solution()

arr = [12, 35, 1, 10, 34, 1]

result = obj.getSecondLargest(arr)

print(result)
