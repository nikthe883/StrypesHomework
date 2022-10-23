from sys import argv
search_list = [30, 40, 50, 52, 56, 62, 70, 91, 100, 131, 132, 166, 170, 195, 202, 205, 212, 248, 249, 256, 263, 272, 288, 289, 290, 296, 332, 345, 352, 364, 380, 390, 407, 412, 429, 430, 438, 444,
               486, 493, 497, 499, 510, 513, 514, 519, 521, 521, 535, 546, 552, 554, 556, 570, 584, 638, 640, 655, 655, 657, 692, 692, 711, 713, 731, 739, 740, 842, 858, 885, 887, 888, 893, 898, 900,
               903, 908, 909, 959, 988]


def binary_search_recursive(searched_list, elem, start=0, end=None):
    if end is None:
        end = len(searched_list) - 1
    if start > end:
        return "not found"

    mid = (start + end) // 2
    if elem == searched_list[mid]:
        return f"found at {mid}"
    if elem < searched_list[mid]:
        return binary_search_recursive(searched_list, elem, start, mid - 1)
    else:
        return binary_search_recursive(searched_list, elem, mid + 1, end)


print(binary_search_recursive(search_list, int(argv[1])))
