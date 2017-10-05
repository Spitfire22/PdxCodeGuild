'''
Lab 11 average numbers
'''


#nums = [5, 0, 8, 3, 4, 1, 6]

# loop over the elements
#for num in nums:
#    print(num)

# loop over the indices
#for i in range(len(nums)):
#    print(nums[i])
nums = []
while True:
    num = input('enter a number, or \'done\': ')
    if num == 'done':
        break
    nums.append(int(num))

print(nums)

print(sum(nums)/len(nums))

