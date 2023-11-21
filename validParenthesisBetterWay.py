class Solution:
    def isValid(self, s: str) -> bool:
        # create a dictionary
        # simple way to create a dictionary
        """
        dic = {}
        dic["{"] = "}"
        dic["("] = ")"
        dic["["] = "]"
        """

        # better way to create a dictionary
        dict2 = {"{": "}", "[": "]", "(": ")"}

        stack = []
        for ele in s:
            if ele in dict2:
                stack.append(ele)
            else:
                if len(stack) == 0:
                    return False
                # top = stack.pop()
                # this way seems more implicit of poping the top
                # seems like the code is more clear is this way
                if dict2[stack.pop()] == ele:
                    continue
                else:
                    return False

        return len(stack) == 0
