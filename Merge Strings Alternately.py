class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        resoult = ''
        if len(word1)>len(word2):
            for position_char_word in range(len(word1)):
                try:
                    resoult  = resoult + word1[position_char_word] + word2[position_char_word]
                except:
                    resoult = resoult + word1[position_char_word]
        else:
            for position_char_word in range(len(word2)):
                try:
                    resoult  = resoult + word1[position_char_word] + word2[position_char_word]  
                except:
                    resoult = resoult + word2[position_char_word]
        return resoult 
        
if __name__ == '__main__':
    word1 = "ab"
    word2 = "pqr"
    print(Solution().mergeAlternately(word1,word2))
