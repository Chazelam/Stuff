def compute_depth(n):
    nums = []
    i = 1
    while len(nums) != 10:
        mult = n*i
        digits = str(mult)
        for digit in digits:
            if (digit in nums) == False:
                nums.append(digit)
        i += 1
    return i - 1
    


#print(compute_depth(1), " = 10")
print(compute_depth(42)," = 9")
