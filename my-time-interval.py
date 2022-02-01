# def map_print(l1, l2):
#     print(l1, l2)

def print_intersection(list_1, list_2):
    l1 = l2 = 0

    l1_len = len(list_1)
    l2_len = len(list_2)
    # print(f"l1_len: {l1_len}, l2_len: {l2_len}")

    while True:
        try:
            if l1 > l1_len and l2 > l2_len:
                break

            l1_start = list_1[l1][0]
            l2_start = list_2[l2][0]
            l1_end = list_1[l1][1]
            l2_end = list_2[l2][1]
            # print(list_1[l1], list_2[l2])

            temp_start = l1_start if l1_start > l2_start else l2_start
            temp_end = l1_end if l1_end < l2_end else l2_end
            # print(f"temp_start: {temp_start}, temp_end: {temp_end}")

            # print(f"temp_start {temp_start}, temp_end: {temp_end}")
            if temp_start <= temp_end:
                print(f"[{temp_start}, {temp_end}]")

            # print(f"l1_end {l1_end}, l2_end: {l2_end}")
            if l1_end < l2_end:
                l1 = l1 + 1
            else:
                l2 = l2 + 1
            # print()
        except IndexError as ex:
            print("ex: ", ex)
            break


arr1 = [[1, 3], [5, 6], [7, 9]]
arr2 = [[2, 3], [5, 7]]
# arr1 = [[1, 3], [5, 7], [9, 12]]
# arr2 = [[5, 10]]

print_intersection(arr1, arr2)
# print(list(map(map_print, arr1,arr2)))
