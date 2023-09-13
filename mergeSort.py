#merge 2 lists and sort them
def mergeAndSort(list1, list2):
    list3 = list1 + list2
    list3.sort()
    print(list3)
mergeAndSort([1,2,30,4,5,6,70,8,9,10], [1,12,13,14,15,16,17,18,19,20])