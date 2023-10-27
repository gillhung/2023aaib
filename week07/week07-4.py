#1 2 4 8 16 32 64 128 256 ...
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:return False #如果n是負的，就錯了!!! 0也是錯的!
        while n>1: #不用除到1，因為1是2的0次方
            if n%2 !=0: #餘數竟然不是0
                return False
            n=n//2

        return True