class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(i):
            if i == 1:
                return 1
            elif i == 2:
                return 2
            elif i < 1:
                return
            
            return climb(i-1) + climb(i-2)

        # return climb(n) 
        if n < 3:
            return n
        a = 1
        b = 2
        c = 0
        for i in range(3,n+1):
            c = a+b
            a = b
            b = c
        
        return c 
