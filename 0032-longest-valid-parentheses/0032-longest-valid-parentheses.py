class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        open_ = close = 0

        for ch in s:
            if ch == '(':
                open_ += 1
            else:
                close += 1
            if open_ == close:
                ans = max(ans, open_ + close)
            elif close > open_:
                open_ = close = 0

        open_ = close = 0

        for ch in reversed(s):
            if ch == '(':
                open_ += 1
            else:
                close += 1
            if open_ == close:
                ans = max(ans, open_ + close)
            elif close < open_:
                open_ = close = 0

        return ans