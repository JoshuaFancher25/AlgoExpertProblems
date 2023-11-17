# given the string of {} [] ()
# determine of the string contains valid parenthesese

class Solution:
    def isValid(self, s: str) -> bool:
        # create a dictionary of parenthese
        dic = {}
        dic["{"] = "}"
        dic["("] = ")"
        dic["["] = "]"
        sStack = []
        for ele in s:
            if ele in dic.values():
                if len(sStack) == 0:
                    return False  ## stack is empty but we have closing parenthese
                top = sStack.pop()
                if dic[top] == ele:
                    continue ## will skip the rest of the for is else and go to the next iteration of the loop
                else:
                    return False ## the parentheses doesn't match in this case
            else:
                sStack.append(ele)
        if len(sStack) == 0:
            return True
        else:
            return False

solution = Solution()
array = "()()()(())}"
print(solution.isValid(array))

