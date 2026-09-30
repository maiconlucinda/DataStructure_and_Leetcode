
# MCMXCIV
# Da esquerda para a direita. 
# Se o valor da esquerda é MAIOR que o valor da direita (M > C), soma o valor de M. O indice anda uma vez.
# Se o valor da esquerda é MENOR que o valor da direita (C < M ), subtraio valor de (M - C) adiciono o resultado e ando duas casas


class Solution:
    def romanToInt(self, s: str) -> int:
        
        dictionary = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400,'D':500, 'CM':900, 'M':1000}

        summ = 0
        idx = 0
        idx_len = len(s)

        while idx < idx_len:
            if idx < idx_len - 1 and dictionary[s[idx]] < dictionary[s[idx+1]]:

                summ += dictionary[s[idx] + s[idx+1]]
                idx += 2
            else:

                summ += dictionary[s[idx]]
                idx +=1

        
        return summ
                




solution = Solution()

result = solution.romanToInt("III")

print(result)