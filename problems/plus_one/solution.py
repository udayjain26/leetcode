class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digStr = ""
        for d in digits:
            digStr+=str(d)
        
        digNum = int(digStr)
        digNum+=1
        digStr = str(digNum)
        finL = []
        for l in digStr:
            finL.append(int(l))
        return finL
        