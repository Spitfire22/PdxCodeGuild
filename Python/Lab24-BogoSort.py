'''

Let's use the most inefficient sorting methods to potentially crash the computer!
Enter Bogo Sort aka 'stupid sort'

'''
import random

# generates and returns a list of length n, with random values between 0 and 100
def random_list(n):
    numb = []
    for i in range(n):
        randnums = random.randint(0, 100)
        numb.append(randnums)
    return numb

# randomly re-arranges a list.
#   iterate through the indices of the list
#   for each index, generate a random index
#   swap the elements at the two indices
def shuffle(nums):
    shuf_list = []
    for i in range(len(nums)):
        new = nums.pop(random.randint(0, len(nums) - 1))
        shuf_list.append(new)
    return shuf_list


# checks if a list is sorted.
#   iterate through the indices of the list
#   if element at current index is greater than the next element.
#       List is not sorted, return false.
#   if you get through the entire list and each element is less than or equal.
#       List is sorted, return true.
def is_sorted(nums):
    for i in range(len(nums)-1):
        j = nums[i+1]
        if nums[i] > j:
            return False
    return True

        # is element[0] less than element[1], while true, compare element 1 less than element 2


#when False, continue to generate random arrangements until the list is sorted
def bogosort(nums):
    count = 0
    while is_sorted(nums) == False:
        nums = shuffle(nums)
        count += 1
    print(count)
    return nums

nums = random_list(10)
print(nums)
print(bogosort(nums))
#is_sorted()
#shuffle()