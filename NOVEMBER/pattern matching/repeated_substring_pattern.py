class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n=len(s)
        for i in range(1,n//2+1):
            if n%i==0:
                j=i
                while j<n and s[j]==s[j%i]:
                    j+=1
                if j==n:
                    return True
        return False