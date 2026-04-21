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

# first occurence in sorted
# class Solution:
#     def fo(self, arr, k):
#         try:
#             return arr.index(k)
#         except ValueError:
#             return -1