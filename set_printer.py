num = input("Enter a number: ")
nums = []

while num != '-1':
    if num.isdigit():
        num = int(num)
        val_nums.append(num)
        if num not in distinct_val_nums:
            distinct_val_nums.append(num)
    else:
        print("invalid")
    num = input("Enter another number: ")

if len(distinct_val_nums) == 0:
    print("No numbers!")
else:
    unique = []
    for i in range(len(nums)-1, -1, -1):
        if nums[i] not in unique:
            unique.append(nums[i])
    for u in unique:
        print(u, end = " ")


    best = nums[0]
    best_count = nums.count(best)
    for n in nums:
        if nums.count(n) > best_count:
            best = n
            best_count = nums.count(n)
    print("Most frequent:", best, "(" + str(best_count) + " times)")

