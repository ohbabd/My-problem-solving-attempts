def quicksort(l):
    if len(l) <= 1:
        return l
    big_list, small_list, pivot = [], [], l.pop()
    while l:
        if l[0] >= pivot:
            big_list.append(l.pop(0))
        else:
            small_list.append(l.pop(0))
        if l:
            if l[-1] <= pivot:
                small_list.append(l.pop())
            else:
                big_list.append(l.pop())
    return quicksort(small_list) + [pivot] + quicksort(big_list)