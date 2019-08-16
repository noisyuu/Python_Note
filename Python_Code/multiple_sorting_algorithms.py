def select_sort(origin_items, comp=lambda x, y: x < y):
    items = origin_items[:]
    for i in range(len(items)-1):
        min_index = i
        for j in range(i+1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def bubble_sort(origin_items, comp=lambda x, y: x > y):
    """高质量冒泡排序(搅拌排序) O(N^2)"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


def merge_sort(items, comp= lambda x, y: x <= y):
    if len(items) < 2:
        return items
    mid = len(items)//2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left,right,comp)


def merge(items1, items2, comp):
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1],items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items


def main():
    origin = [1,3,5,1,5,123,7,8,9,32,4,123,5,2,55,5566,333,345,33,7,34,5,345,12,4,5,6,2342,2354,323,23425,32356,434534,5654,23]
    '''''''#items = select_sort(origin)'''''''
    #items = bubble_sort(origin)
    #items = origin[:]
    items = merge_sort(origin)
    print(items)



if __name__ == '__main__':
    main()



