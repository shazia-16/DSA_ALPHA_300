class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n=len(s)
        if len(goal)!=n:
            return False
        doubled=s+s
        for i in range(n):
            j=0
            while j<n and doubled[i+j]==goal[j]:
                j+=1
            if j==n:
                return True
        return False