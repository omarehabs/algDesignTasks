def merge_sort(list):
    n = len(list)
    if (n < 2):
        return

    mid = (n + 1)//2
    left, right = list[:mid],  list[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            list[k] = left[i]
            i += 1
        else:
            list[k] = right[j]
            j += 1
        k += 1

    if i < len(left):
        list[k] = left[i]
        i += 1
        k += 1

    if j < len(right):
        list[k] = right[j]
        j += 1
        k += 1


list = [8, 2, 3]

merge_sort(list)
print(list)
