def bubble_sort(unsorted):
    """
    Bubblesort
    
    Can sort simple list
    >>> bubble_sort([3,2,1])
    [1, 2, 3]

    Behaves like std sort
    >>> bubble_sort([7,2,6,1,-3,99,3]) == sorted([7,2,6,1,-3,99,3])
    True
    """
    if len(unsorted) < 2:
        return unsorted

    for i in range(1, len(unsorted)):
        for j in range(len(unsorted)-2, i-2, -1):
            if unsorted[j] > unsorted[j+1]:
                unsorted[j+1], unsorted[j] = unsorted[j], unsorted[j+1]
    return unsorted

def quick_sort(sort_me, left=None, right=None, quicksort_limit=3):
    """
    Quicksort
    
    Can sort simple list
    >>> quick_sort([3,2,1])
    [1, 2, 3]

    Behaves like std sort
    >>> quick_sort([7,2,6,1,-3,99,3]) == sorted([7,2,6,1,-3,99,3])
    True

    Falls back to linear sorting for lists less than 3 elements
    >>> quick_sort([2,1]) == sorted([2,1])
    True
    """

    def pivot(sort_me, left, right):
        #median method
        middle = (left + right) // 2
        return min(max(sort_me[left], sort_me[middle]), sort_me[right])

    def partition(sort_me, left, right, k):
        partition_val = k
        i = left
        j = right

        while True:
            while i < right and sort_me[i] < partition_val:
                i = i + 1
            while j > left and sort_me[j] > partition_val:
                j = j - 1

            if j <= i:
                break
            sort_me[i], sort_me[j] = sort_me[j], sort_me[i]

        return j

    # this block is for top-level call, where left and right are undefined
    left = left or 0
    right = right or len(sort_me) - 1

    # do a linear sort if sublust length is below limit
    if (right - left) < quicksort_limit:
        # with bubblesort
        # for i in range(left, right):
        #     for j in range(right-1, i-1, -1):
        #         if sort_me[j] > sort_me[j+1]:
        #             sort_me[j+1], sort_me[j] = sort_me[j], sort_me[j+1]
        # with insertion sort
        for i in range(left+1, right+1):
            tmp = sort_me[i]
            j = i - 1
            while j >= 0 and sort_me[j] > tmp:
                sort_me[j+1] = sort_me[j]
                j = j - 1
            sort_me[j+1] = tmp
    else:
        pivot_value = pivot(sort_me, left, right)
        partition_point = partition(sort_me, left, right, pivot_value)
        sort_me = quick_sort(sort_me, left=left, right=partition_point-1)
        sort_me = quick_sort(sort_me, left=partition_point+1, right=right)
    return sort_me

def bogo_sort(unsorted):
    """
    Bogosort as a joke
    
    Can sort simple list
    >>> bogo_sort([3,2,1])
    [1, 2, 3]

    Behaves like std sort
    >>> bogo_sort([7,2,6,1,-3,99,3]) == sorted([7,2,6,1,-3,99,3])
    True
    """

    def _is_sorted(_input_list) -> bool:
        was_sorted = True
        for i in range(1, len(_input_list)):
            was_sorted = was_sorted and (_input_list[i-1] <= _input_list[i])
        return was_sorted

    def _seq_generator(_input_list):
        from random import randint
        while len(_input_list):
            random_idx = randint(0, len(_input_list)-1)
            yield _input_list.pop(random_idx)

    bogo_list = unsorted[:]
    while not _is_sorted(bogo_list):
        bogo_list = [e for e in _seq_generator(unsorted[:])]

    return bogo_list

def insertion_sort(unsorted):
    """
    Insertion sort

    Can sort
    >>> insertion_sort([3,2,1])
    [1, 2, 3]

    Behaves like std sort
    >>> insertion_sort(list('REKURSIO')) == sorted(list('REKURSIO'))
    True
    >>> insertion_sort([7,2,6,1,-3,99,3]) == sorted([7,2,6,1,-3,99,3])
    True
    """
    for i in range(1, len(unsorted)):
        tmp = unsorted[i]
        j = i - 1
        while j >= 0 and unsorted[j] > tmp:
            unsorted[j+1] = unsorted[j]
            j = j - 1
        unsorted[j+1] = tmp
    return unsorted

def selection_sort(unsorted):
    """
    Selection sort

    Can sort
    >>> selection_sort([3,2,1])
    [1, 2, 3]

    Behaves like std sort
    >>> selection_sort(list('REKURSIO')) == sorted(list('REKURSIO'))
    True
    >>> selection_sort([7,2,6,1,-3,99,3]) == sorted([7,2,6,1,-3,99,3])
    True
    """
    for i in range(len(unsorted)):
        k = i
        for j in range(i+1, len(unsorted)):
            if unsorted[j] < unsorted[k]:
                k = j
        if k != i:
            unsorted[k], unsorted[i] = unsorted[i], unsorted[k]
    return unsorted

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, exclude_empty=True)