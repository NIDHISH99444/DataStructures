class Solution(object):

    def noOftimesArrayRotated(self, arr):

        start = 0
        end = len(arr) - 1
        if arr[start] < arr[end]:
            return 0

        while start <= end:
            mid = start + (end - start) // 2
            prev = (mid + len(arr) - 1) % (len(arr))
            next = (mid + 1) % len(arr)
            if arr[mid] <= arr[prev] and arr[mid] <= arr[next]:
                return mid
            elif arr[mid] >= arr[start]:
                start = mid + 1
            elif arr[mid] <= arr[end]:
                end = mid - 1

    def findElementIncreasing(self, arr, ele, start, end):
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == ele:
                return mid
            elif arr[mid] > ele:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def search(self, arr, key):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(arr) == 0:
            return -1
        index = self.noOftimesArrayRotated(arr)
        resL = self.findElementIncreasing(arr, key, 0, index)
        resR = self.findElementIncreasing(arr, key, index, len(arr) - 1)
        if resL == -1:
            return resR
        else:
            return resL

arr = [3, 1]
s=Solution()
#print(s.search(arr, 0))


def canAllocate(arr,student,mid):
    stu=1
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
        if sum>mid:
            stu+=1
            if stu>students:
                return False
            else:
                sum=arr[i]
    return True

def allocateBooks(arr,students):
    res=-1
    start=max(arr)
    end=sum(arr)
    while start<=end:
        mid=start+(end-start)//2
        if canAllocate(arr,students,mid):
            res=mid
            end=mid-1
        else:
            start=mid+1
    return res


arr=[5, 17, 100, 11]
students=4
print(allocateBooks(arr,students))