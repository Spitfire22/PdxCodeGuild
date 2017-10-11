'''

Lab 20 - validating the credit card you found in the hallway - is it real? or is it a setup?

'''

def validate(nums):
    nums = list(nums)
    for i in range(len(nums)):
        nums[i] = int(nums[i])
###    nums = list(map(lambda x: int(x), nums)) ### Nick showed me this function - a little more advanced.
    complete = nums
    check_digit = nums.pop(15)
    nums = (nums[::-1])
    for i in range(0, len(nums), 2):
        nums[i] *= 2
    print(nums)
    #step5 - not working!
    for elem in nums:
        if elem >= 9:
            elem -= 9
    print(nums)


    return



# suspect = [7178908434234538] # this is my made up list
copied = "4556737586899855" # this is out of the lab instructions

validate(copied)