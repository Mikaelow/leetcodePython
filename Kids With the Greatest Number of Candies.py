class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        i = 0
        resoults = []
        while i <= len(candies)-1:
            j = 0
            while j<i:
                if candies[j] == candies[i]:
                    resoults.append(resoults[j])
                    break
                j = j+1
            if (candies[i]+extraCandies > candies[i-1]+extraCandies or i == 0) and len(resoults) == i:
                resoults.append(True)
            elif candies[i]+extraCandies < candies[i-1]+extraCandies and len(resoults) == i:
                resoults.append(False)          
            i = i + 1
        return resoults
        


if __name__ == '__main__':
    candies = [4,2,1,1,2]
    extraCandies = 1
    print(Solution().kidsWithCandies(candies,extraCandies))