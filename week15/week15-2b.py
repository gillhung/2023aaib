class Solution:
    def maxScore(self, s: str) -> int:
        N=len(s)
        zero=0
        one=0
        for i in range(N):
            if s[i]=='1':one+=1 # 如果是1，先全部加起來
        #現在就知道總共有幾個one
        ans=0
        for i in range(N-1):
            if s[i]=='0':
                zero+=1
            if s[i]=='1':
                one-=1
            ans=max(ans,zero+one)
        return ans