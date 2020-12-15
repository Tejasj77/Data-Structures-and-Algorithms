class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = []

        start = 0
        count = 0
        for idx, char in enumerate(S):
            count += 1 if char == '(' else -1
            if count == 0:
                print(idx,char,S[start + 1:idx])
                result.append(S[start + 1:idx])
                print(result)
                start = idx + 1

        return "".join(result)

S=Solution()
ans = Solution.removeOuterParentheses(S,S='(()())(())')
print(ans)