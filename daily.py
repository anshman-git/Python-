# 1.print all prime factor (g4g)
# class Solution:
#     def primeFac(self, n):
#         # code here
#         factor = []
#         i = 2
        
#         while n>1:
#             if n%i == 0:
#                 if(i not in factor):
#                     factor.append(i)
#                 n=n//i
#             else:
#                 i+=1
#         return factor