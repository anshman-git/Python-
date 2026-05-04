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


# 2. Array Duplicate
# def arraydup(arr):
#     duplicates = []
#     for x in arr:
#         index = abs(x) - 1
#         if arr[index] < 0:
#             duplicates.append(abs(x))
#         else:
#             arr[index] *= -1
#     return duplicates

# 3.Missing and Duplicate
# class Solution:
#     def findTwoElement(self, arr):
#         dup = []
#         seen = set()
#         n = len(arr)
#         for num in arr:
#             if num in seen:
#                 dup.append(num)
#             else:
#                 seen.add(num)
#         total = (n * (n + 1)) // 2
#         actual = sum(arr)
#         missing = total - (actual - dup[0])
#         dup.append(missing)
#         return dup

# 4.Counts Digits
#User function Template for python3

# class Solution:
#     def evenlyDivides(self, n):
#         count = 0
#         temp = n
#         while temp > 0:
#             digit = temp % 10
#             if digit != 0 and n % digit == 0:
#                 count += 1
#             temp //= 10
#         return count

# 5.Write a program to print multiplication table of n using for loops in reversed order.
# def multiplication_table(n):
#                 for i in range(1, 11):
#                         print(f"{n} x {11-i} = {n * (11-i)}")

# n = int(input("Enter any number: "))
# multiplication_table(n)

# 6.Move all zero to the end (g4g)
# class Solution:
# 	def pushZerosToEnd(self, arr):
#     	count = 0 
        
#         for i in range(len(arr)):
#             if arr[i] != 0:
#                 arr[count] = arr[i]
#                 count += 1
        
#         while count < len(arr):
#             arr[count] = 0
#             count += 1

# 7.Sum 1 to n divisor
# class Solution:
    # def sumOfDivisors(self, n):
    #     total_sum = 0
    #     for i in range(1, n + 1):
    #         total_sum += (n // i) * i
    #     return total_sum

# 8
# first occurence in sorted
# class Solution:
#     def fo(self, arr, k):
#         try:
#             return arr.index(k)
#         except ValueError:
#             return -1

# 9
# Equillibrium point
# class Solution:
#     def findEquilibrium(self, arr):
#         # code here
#         total=sum(arr)
#         left_sum=0
#         for i in range(len(arr)):
#             right_sum=total-left_sum-arr[i]
#             if(left_sum  ==  right_sum):
#                 return i;
#             left_sum+=arr[i]
#         return -1


#10
# count vovel
# def count_vowels(text):
#     count = 0
#     for ch in text:
#         if ch in "aeiouAEIOU":
#             count += 1
#     return count

# 11
# Union of two array (g4g)
# class Solution:
#     def findUnion(self, a, b):
#         # code here 
#         i=0
#         res=[]
#         seen=set()
#         while(i<len(a) or i<len(b)):
#             if(i<len(a) and a[i] not in seen):
#                 seen.add(a[i])
#                 res.append(a[i])
#             if(i<len(b) and b[i] not in seen):
#                 seen.add(b[i])
#                 res.append(b[i])
            
#             i+=1
#         res.sort()
#         return res

# 12
# Armstrong number
# class Solution:
#     def armstrongNumber (self, n):
#         # code here 
#         arm=0
#         num=n
#         while(num!=0):
#             digit= num%10
#             num=int(num/10)
#             arm+=digit*digit*digit
#         if(arm==n):
#             return True
#         else:
#             return False

# 13
# Third Largest
# class Solution:
#     def thirdLargest(self,arr):
#         # code here
#         lens=len(arr)
#         if(lens<3):
#             return -1
#         arr.sort()
#         return arr[lens-3]