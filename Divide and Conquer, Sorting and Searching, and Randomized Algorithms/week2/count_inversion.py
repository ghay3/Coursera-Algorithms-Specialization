def sort_and_count_inversion(nums):
    if len(nums) <= 1:
        return nums or [], 0

    mid = len(nums) // 2
    sorted_left, count_left = sort_and_count_inversion(nums[:mid])
    sorted_right, count_right = sort_and_count_inversion(nums[mid:])
    return merge_and_count_split_inversion(sorted_left, sorted_right, count_left, count_right)


def merge_and_count_split_inversion(sorted_left, sorted_right, count_left, count_right):
    merged, split_count = [], 0
    i, j, k = 0, 0, len(sorted_left) + len(sorted_right)
    for _ in range(k):
        if j == len(sorted_right):
            merged.append(sorted_left[i])
            i += 1

            split_count += j
            for num in sorted_right[:j]:
                print((sorted_left[i-1], num))
        elif i == len(sorted_left):
            merged.append(sorted_right[j])
            j += 1
        elif sorted_left[i] <= sorted_right[j]:
            merged.append(sorted_left[i])
            i += 1

            split_count += j
            for num in sorted_right[:j]:
                print((sorted_left[i-1], num))
        else:
            merged.append(sorted_right[j])
            j += 1
    return merged, split_count + count_left + count_right


if __name__ == '__main__':
    nums = [1, 3, 5, 2, 4, 6]
    _, count = sort_and_count_inversion(nums)
    print('total:', count)
    assert(count == 3)

    nums = [6, 5, 4, 3, 2, 1]
    _, count = sort_and_count_inversion(nums)
    print('total:', count)
    assert (count == 15)
