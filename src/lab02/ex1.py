def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise 'ValueError'
    min1 = min(nums)
    max1 = max(nums)
    return (min1, max1)

print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([1.5, 2, 2.0, -3.1]))
print(min_max([]))
