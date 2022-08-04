def maxLength(self, S):
        ls = []
        ls.append(-1)
        max1 = 0
        for i in range(len(S)):
            if (S[i] == "("):
                ls.append(i)
            else:
                if (len(ls) != 0):
                    ls.pop()
                if (len(ls) == 0):
                    ls.append(i)
                max1 = max(max1, i - ls[-1])
        return max1
