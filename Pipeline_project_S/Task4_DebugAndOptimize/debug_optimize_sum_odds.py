def sum_odds(numbers):
    return sum(num for num in numbers if num % 2)

nums = [1, 2, 3, 4, 5]
print(sum_odds(nums))

