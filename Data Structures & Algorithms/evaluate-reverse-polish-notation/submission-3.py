class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for i in range(len(tokens)):
            if tokens[i] not in "+-/*":
                res.append(int(tokens[i]))
            else:
                b = res.pop()
                a = res.pop()
                if tokens[i] == "+":
                    res.append(a+b)
                elif tokens[i] == "*":
                    res.append(a*b)
                elif tokens[i] == "-":
                    res.append(a-b)
                else:
                    res.append(int(a/b))
        return res[0]