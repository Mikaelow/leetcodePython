from collections import Counter

def mergeTwoLists(self, list1, list2):
    counterList1 = Counter(list1)
    counterList2 = Counter(list2)
    newList = []
    for i in range(10):
        if counterList1[i] != 0:
            for number in range(counterList1[i]):
                newList.append(i)
        if counterList2[i] != 0:
            for number in range(counterList2[i]):
                newList.append(i)
    return newList
list1 = []
list2 = [0]

print(mergeTwoLists('', list1, list2))