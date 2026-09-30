# Aqui é lista de pares porque eu nunca busco por chave. Eu percorro do maior pro menor subtraindo, então o que eu preciso é a ordem, não lookup. Dict não me daria vantagem nenhuma.

class Solution:
    def intToRoman(self, num: int) -> str:
        symList = [
            ["I", 1], 
            ["IV", 4], 
            ["V", 5], 
            ["IX", 9], 
            ["X", 10], 
            ["XL", 40], 
            ["L", 50], 
            ["XC", 90], 
            ["C", 100], 
            ["CD", 400], 
            ["D", 500], 
            ["CM", 900], 
            ["M", 1000]]

        
        res = ""
        for symbol, value in reversed(symList):
            
            if num // value:

                # Divido o 
                count = num // value
                res = (symbol * count)

                # Atualizo a variável num, agora num é igual ao resto.
                num = num % value
        return res

solution = Solution()

print(solution.intToRoman(700))