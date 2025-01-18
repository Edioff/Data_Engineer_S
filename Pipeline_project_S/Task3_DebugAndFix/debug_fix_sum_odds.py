def sum_odds(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 1:
            total += num
    return total

nums = [-1,-2,-3,1, 2, 3, 4, 5]
print(sum_odds(nums))

