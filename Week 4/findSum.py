def findSum(nums, n, target):
    highIndex = n - 1
    lowIndex = 0
    for i in range(n-1):
        if (nums[highIndex] + nums[lowIndex] == target): #find target
            break
        elif(nums[highIndex] + nums[lowIndex] < target): #sum to less than target
            lowIndex += 1
        elif(nums[highIndex] + nums[lowIndex] > target): #sum to more than target
            highIndex -= 1
        else: #target is unobtainable
            return None

    return [lowIndex, highIndex]


nums = [1, 2, 3, 4, 5, 6, 7]
nums2 = [1, 5, 7, 10, 11, 17, 22]
nums3 = [1,2,3,4,5]

print(findSum(nums, 7, 7))
print(findSum(nums2, 7, 24))
print(findSum(nums, 7, 20))
print(findSum(nums3, 5, 0))