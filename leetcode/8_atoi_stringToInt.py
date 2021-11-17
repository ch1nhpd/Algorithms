class Solution:
    def myAtoi(self, s: str) -> int:
        rs = 0
        flag = 0 # dùng để đánh dấu xem đã gặp dấu cộng, trừ hoặc bắt đầu tính số chưa
        for i in s:
            ii = ord(i)
            if i ==' ' and flag==0:
                continue
            elif (i =='+' or i =='-') and flag == 0:
                flag = -1 if i=='-' else 1
            elif ii >=48 and ii <=57:
                if flag ==0: 
                    flag = 1
                rs = rs*10+ (ii-48)
                if rs > 2**31-1:
                    return 2147483647 if flag>0 else -2147483648
            else:
                break
        return rs if flag>0 else -rs