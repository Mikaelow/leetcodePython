from typing import List


class SolNR27:
    def removeElement(self, list: List[int], val:int):
        while val in list:
            list.remove(val)
