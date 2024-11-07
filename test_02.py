def search(nums: list[int], target: int) -> int:
    # *guard clauses ------------------
    if len(nums) == 0:
        return -1

    if len(nums) == 1:
        if nums[0] == target:
            return 0
        return -1
    # * --------------------------------

    first = 0
    last = len(nums) - 1

    # *guard clauses -------------------
    if nums[first] == target:
        return first

    if nums[last] == target:
        return last
    # * --------------------------------
    skip = False
    if nums[last] > nums[0]:
        skip = True

    # skip if values are all in sorted order
    if skip == False:
        idx = 0
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                idx = i
                break

        mid = idx
        if target > nums[0]:
            last = mid
        if target < nums[0]:
            first = mid + 1

    while first < last:
        mid = first + (last - first) // 2
        if nums[first] == target:
            return first
        if nums[mid] == target:
            return mid
        if nums[last] == target:
            return last

        if nums[mid] > target:
            last = mid
        if nums[mid] < target:
            first = mid + 1

    return -1


def main() -> None:
    print(search(nums=[1, 3, 5], target=3))


if __name__ == '__main__':
    main()
