class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        i = 1 
        j = 0
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        elif len(flowerbed) == 1 and flowerbed[0] == 1 :
            return False
        else:
            while i < len(flowerbed)-1:
                if  flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    j = j + 1
                    i = i + 1
                elif i == 1 and flowerbed[i-1] == 0 and flowerbed[i] == 0:
                    j = j + 1
                elif i == len(flowerbed)-2 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    j = j + 1
                i = i + 1
        if j >= n:
            return True
        else:
            return False



if __name__ == '__main__':
    flowerbed = [0]
    n = 1
    print(Solution().canPlaceFlowers(flowerbed,n))