from typing import List


class SolNR2:
    def addTwoNumbers(self,list1: List[int],list2: List[int]):
        summedList = []
        lenOfLonger=max(len(list1),len(list2))+2
        sumOfLists = 0
        for i in range(1,lenOfLonger):
            if i > len(list2):
                list2.append(0)
            if i > len(list1):
                list1.append(0)
            sumOfLists =sumOfLists+list1[-i]+list2[-i]
            if sumOfLists > 9:
                summedList.append(sumOfLists-10)
                sumOfLists=1
            else:
                summedList.append(sumOfLists)
                sumOfLists = 0
        return summedList
