'''

Lab 21 - Peaks, valleys, and alpine lakes. Wim Hof that lake!

'''

# with the peaks, we are comparing indices where the numbers on either side are less than through the index
# if one side is higher or lower than the center variable, skip, center variable must be greatest.
def peaks(nums):
    top = []
    for i in range(1, len(nums)-1):
        j = nums[i+1]
        h = nums[i-1]
        if nums[i] > j and nums[i] > h:
            top.append(i)
    return top

# with the valleys we are comparing indices where the numbers on either side are greater than through the index
# if one side is higher or lower than the center variable, skip, center variable must be lowest.
def valleys(nums):
    bottom = []
    for i in range(1, len(nums)-1):
        j = nums[i+1]
        h = nums[i-1]
        if nums[i] < j and nums[i] < h:
            bottom.append(i)
    return bottom

# take both peaks and valleys and compile a new list including both
def peaks_and_valleys(nums):
    list = peaks(nums)
    list.extend(valleys(nums))
    return list


# display with 'X' the 'height' of each data point.
def display():
    pass

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print(data)
print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))


