# https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self,x, y):
        c = bin(x)
        d = bin(y)
        (c1,c2)=c.split('b') #将二进制分割，我们仅需要'0b'右边的有效数字
        (d1,d2)=d.split('b')
        #通过下述代码来达到两个二进制数能够相互对齐的目的。
        if len(c2)>len(d2):
            d3 = d2.zfill(len(c2))# 这里zfill()函数是返回，并不是将d2修改，这里不要犯错。
            c3 = c2
        else:
            c3 = c2.zfill(len(d2))
            d3 = d2
        countall = 0
        number = 0
        for i in c3:# 进行计算hamming distance
            if i != d3[number]:
                countall+=1
            number+=1
        return countall
