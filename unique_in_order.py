def unique_in_order(iterable):
    arr = list(iterable)
    # turns the string into a list.
    new_arr = []
    # sets up where answer will go.
    count = len(arr)
    # the number of items in the arr.
    for n in arr:
        count -= 1
        # count decreases per item in arr.
        if arr[count] != arr[count-1]:
            new_arr.append(arr[count])
            # adds the first value to new_arr if two values are not the same.
        elif len(arr) == 1:
            new_arr.append(arr[0])
            # if arr only has one item, adds it to new_arr.
        elif len(set(arr))==1:
            arr.remove(arr[0])
            new_arr.append(arr[0])
            # if arr has duplicates of the same item, deletes the duplicate from arr and adds the remaining new_arr.

    return new_arr[::-1]

iterable = "AA"

print(unique_in_order(iterable))
