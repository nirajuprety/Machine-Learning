# list_a = [1, 2, 3, 4, 5]
# list_b = [10, 20, 30, 40, 50, 60]
# print(list_a)
# print(list_b)
# # for i in list_b:
# #     if i % 2 == 1:
# #         print("hello")
# #         print(list_a.extend(list_b[i]))

# list_a = [i if i % 2 == 1 else 0 for i in list_b]
# print(list_a)


# new_list = list1 + [list2[x] for x in range(len(list2)) if x % 2 != 0]


def mergingList(lista: list, listb: list) -> list:
    """
    This function takes two lists as arguments and
    returns a new list merging first list with the
    odd indexes of second list.

    Args:
        lista (list): first list of numbers
        listb (list): second list of numbers

    Returns:
        list: new list formed by first list extended
        with odd indexes of second list
    """
    new_list = lista + [listb[x] for x in range(len(listb)) if x % 2 != 0]
    return new_list


lista = [1, 2, 3, 4, 5, 6]  # defined first list
listb = [10, 20, 30, 40, 50, 60]  # defined second list
print(mergingList(lista, listb))  # merge_list function call
