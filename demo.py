# Find list index if sum of two digits in the list is match with target value.
# nub = [2, 7, 11, 15] target = 9
# output : [0,1]

# nub = [2, 7, 1, 15, 8] target = 9
# output : [0,1, 2, 4]

num = [2, 7, 11, 15]

a = 0
sum1 = 9
#output = [0,1]

for i in range(len(num)-1):
    #a = num[i] + num[i+1]
    if(num[i] + num[i+1] == sum1):
        print(num.index(num[i]),num.index(num[i+1]))

