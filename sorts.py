arr = [5, 43, 8, 1, 12, 96, 30]


def InsertionSort(arr: list, insert_method: str = 'element') -> list:
    # if insert_method == 'element':
    #     for i in range(1, len(arr)):
    #         j = 1
    #         while j > 0 and arr[j] < arr[j - 1]:
    #             arr[j], arr[j - 1] = arr[j - 1], arr[j]
    #             j -= 1
    # element insertion don't working
    if insert_method == 'binary':
        for i in range(1, len(arr)):

            l = 0
            r = i
            m = 0
            while l != r:
                m = (l + r) // 2
                if arr[i] < arr[m]:
                    r = m
                else:
                    l = m + 1
            if arr[i] > arr[m]:
                m += 1
            arr.insert(m, arr[i])
            arr.pop(i + 1)
    return arr