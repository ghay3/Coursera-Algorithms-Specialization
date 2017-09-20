import random
from statistics import median


def quick_sort(nums):
    _quick_sort(nums, 0, len(nums)-1)
    return nums


def _quick_sort(nums, low, high):
    if high <= low:
        return

    mid = partition(nums, low, high)
    _quick_sort(nums, low, mid-1)
    _quick_sort(nums, mid+1, high)


def partition(nums, low, high):
    pivot = random_as_pivot(nums, low, high)
    i = j = low + 1
    while j <= high:
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
    nums[low], nums[i-1] = nums[i-1], nums[low]
    return i - 1


def first_as_pivot(nums, low, high):
    return nums[low]


def last_as_pivot(nums, low, high):
    nums[low], nums[high] = nums[high], nums[low]
    return nums[low]


def median_of_three_as_pivot(nums, low, high):
    mid = low + (high - low) // 2
    median_val = median([nums[low], nums[mid], nums[high]])
    for idx in (low, mid, high):
        if nums[idx] == median_val:
            nums[idx], nums[low] = nums[low], nums[idx]
            break
    return nums[low]


def random_as_pivot(nums, low, high):
    chosen = random.randint(low, high)
    nums[low], nums[chosen] = nums[chosen], nums[low]
    return nums[low]


if __name__ == '__main__':
    nums = []
    for i in range(100):
        nums.append(i)
        random.shuffle(nums)
        algorithm_result = quick_sort(nums)
        correct_result = sorted(nums)
        if algorithm_result != correct_result:
            print('mismatch for nums:', nums)
            break
