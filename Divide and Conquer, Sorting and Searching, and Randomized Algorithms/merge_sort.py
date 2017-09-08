import random


# https://en.wikipedia.org/wiki/Merge_sort
def merge_sort(nums):
    if len(nums) <= 1:
        return nums or []

    m = len(nums) // 2
    left = merge_sort(nums[:m])
    right = merge_sort(nums[m:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j, k = 0, 0, len(left) + len(right)
    for _ in range(k):
        if j == len(right):
            result.append(left[i])
            i += 1
        elif i == len(left):
            result.append(right[j])
            j += 1
        elif left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result


if __name__ == '__main__':
    nums = []
    for i in range(100):
        nums.append(i)
        random.shuffle(nums)
        merge_result = merge_sort(nums)
        correct_result = sorted(nums)
        if merge_result != correct_result:
            print('mismatch for nums:', nums)
            break
