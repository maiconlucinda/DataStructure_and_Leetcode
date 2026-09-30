class Solution:
    def isValid(self, s: str) -> bool:
        
        # Crio uma stack para 
        stack = []
        closeToOpen = { ")": "(",
                                        "]": "[",      
                                        "}": "{" 
                                    }

        for symbol in s:
            if symbol in closeToOpen.keys():
                if stack and stack[-1] == closeToOpen[symbol]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(symbol)
        
        return True if not stack else False
    

solution = Solution()
print(solution.isValid("{([])}"))

