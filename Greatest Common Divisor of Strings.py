class Solution:
    def resoult(self, word_to_divide:str):
        divisor = 1
        while len(word_to_divide)>=divisor:
            start_of_string = 0
            end_of_string = divisor

            if len(word_to_divide)%divisor == 0:
                memory = word_to_divide[start_of_string:end_of_string]

                while end_of_string<=len(word_to_divide):
                    if  memory == word_to_divide[start_of_string:end_of_string]:
                       if end_of_string == len(word_to_divide):
                           return memory
                       start_of_string = start_of_string + divisor
                       end_of_string = end_of_string + divisor
                    else:
                        break
            else:
                pass
            divisor = divisor + 1


    def gcdOfStrings(self, str1: str, str2: str):
        result1 = self.resoult(str1)
        result2 = self.resoult(str2)
        if result1 == result2:
            return result1
        else:
            return ''

    


if __name__ == '__main__':
    str1 = "ABCABC"
    str2 = "ABC"
    print(Solution().gcdOfStrings(str1,str2)) 