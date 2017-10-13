'''

Lab 20 - validating the credit card you found in the hallway - is it real? or is it a setup?

'''

def validate(nums):
    nums = list(nums)
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    print('Original list: ', nums)
###    nums = list(map(lambda x: int(x), nums)) ### Nick showed me this function - a little more advanced.
    check_digit = nums.pop(15)
    print('Remove last number: ', nums)
    nums = (nums[::-1])
    print('Reverse list: ', nums)
    for i in range(0, len(nums), 2):
        nums[i] *= 2
    print('Every other number * 2: ',nums)
    for i in range(len(nums)):
        while nums[i] > 9:
            nums[i] -= 9
    print('Subtract 9 from all numbers above 9: ', nums)
    strnums = str(nums)
    addnums = sum(nums)
    print('Sum of all values: ',addnums)
    addnums = addnums % 10
    print('Second digit of sum: ',addnums)
    print('Is the card Valid or not? ',addnums == check_digit)
    return




suspect = "2646976047629706" # this is my made up list
suspect2 = "4149264471442128" # another made up list
copied = "4556737586899855" # this is out of the lab instructions

#validate(copied)
validate(suspect2)