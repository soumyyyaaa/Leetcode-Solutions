def mergeTwoLists(list1, list2):
    listMerge = []
    listMerge = listMerge + list1 + list2
    for i in range(0, len(listMerge) - 1):
        for j in range(0, len(listMerge) - i - 1):
            if listMerge[j] > listMerge[j+1]:
                listMerge[j], listMerge[j + 1] = listMerge[j + 1], listMerge[j]
    
    return listMerge
    
list1 = [1,2,4]
list2 = [1,3,4]
print(mergeTwoLists(list1, list2))