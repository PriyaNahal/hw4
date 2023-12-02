def merge_list(list1, list2):
    for element in list1:
        if not isinstance(element, int):
            raise TypeError("Bad Input")
    for element in list2:
        if not isinstance(element, int):
            raise TypeError("Bad Input")

    merged = []

    i = 0
    j = 0
    num1 = len(list1)
    num2 = len(list2)

    while i < num1 and j < num2:
        if list1[i] > list2[j]:
            merged.append(list2[j])
            j += 1
        else:
            merged.append(list1[i])
            i += 1

    merged.extend(list1[i:])
    merged.extend(list2[j:])

    new_list = merged
    list_length = len(new_list)

    for k in range(list_length):
        for h in range(0, list_length - k - 1):
            if new_list[h] > new_list[h + 1]:
                new_list[h], new_list[h + 1] = new_list[h + 1], new_list[h]

    return merged

