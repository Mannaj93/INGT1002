def separate(numbers, threshold):
    list1 = []
    list2 = []
    for i in numbers:
        if i < threshold:
            list1 . append(i)
        else:
            list2 . append(i)
    return list1, list2
separate(3,4)