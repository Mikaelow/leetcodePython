class Solution:
    def __maxStringFinder(arr:list):
        index = 0
        for i in range(len(arr)):
            if int(arr[index]) <= int(arr[i]): 
                index = i
        return arr[index]

    def intConverter(s:str):
        c = ''
        arr = []
        for char in s:
            if ord(char) in range(47,58): c +=char
            else: 
                arr.append(c)
                c = ''
        arr.append(c)
        return Solution.__maxStringFinder(arr)



s = '42_1231_9814685_9814686_9814683'
sol = Solution.intConverter(s)
print(sol)