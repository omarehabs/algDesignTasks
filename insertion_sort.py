def insertion_sort(items):
    n = len(items)

    for i in range(n):
        j = i
        while j > 0 and items[j] < items[j - 1]:
            items[j], items[j-1] = items[j - 1], items[j]
            j -= 1

    return items


sorted = insertion_sort([2, 3, 6, 1])
print(sorted)
