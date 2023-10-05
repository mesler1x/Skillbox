nums = input()
first_idx = nums.find(" ")
second_idx = nums.find(" ", first_idx + 1)
num1 = int(nums[:first_idx])
num2 = int(nums[first_idx + 1:second_idx])
num3 = int(nums[second_idx + 1:])

if (num1 > num2):
    if (num3 > num1):
        print(num1)
    elif (num3 > num2):
        print(num3)
    else:
        print(num2)
elif(num3 > num2):
    print(num2)
else:
    if (num1 > num3):
        print(num1)
    else:
        print(num3)
