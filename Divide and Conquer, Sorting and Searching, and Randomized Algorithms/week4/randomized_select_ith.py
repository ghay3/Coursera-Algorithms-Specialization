import random


# https://en.wikipedia.org/wiki/Quickselect
def select_ith(nums, i):
    return _select_ith(nums, 0, len(nums)-1, i)


def _select_ith(nums, low, high, i):
    if low == high:
        return nums[low]

    j = partition(nums, low, high)
    k = j - low + 1
    if k < i:
        return _select_ith(nums, j+1, high, i-k)
    elif k > i:
        return _select_ith(nums, low, j-1, i)
    else:
        return nums[j]


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


def random_as_pivot(nums, low, high):
    chosen = random.randint(low, high)
    nums[low], nums[chosen] = nums[chosen], nums[low]
    return nums[low]


if __name__ == '__main__':
    nums = []
    for num in range(100):
        nums.append(num)
        random.shuffle(nums)
        i = random.randint(0, num)
        algorithm_result = select_ith(nums, i + 1)
        correct_result = i
        if algorithm_result != correct_result:
            print('mismatch for nums:', nums)
            print('searching for i:', i)
            break