class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split(" ")
        for w in reversed(x):
            if len(w) != 0:
                return len(w)
