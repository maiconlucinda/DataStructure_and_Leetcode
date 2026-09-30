class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        
        for index in range(len(strs[0])): # pego a primeira palavra e crio um range

            for word in strs: # pego cada palavra da lista 

                if index == len(word) or word[index] != strs[0][index]:
                    return result

            result += strs[0][index]
        
        return result
    

solution = Solution()

print(solution.longestCommonPrefix(["flower","flow","flight"]))