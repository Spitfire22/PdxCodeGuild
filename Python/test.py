## Test

#num = 3.123123123
#print(num)

###############################

import random
digits = []
ii = 0
while ii < 6:
    lotto = random.randint(1, 99)
    digits.append(int(lotto))
    ii = ii + 1
print('These are the winning Lottery numbers:', digits)

print(digits)