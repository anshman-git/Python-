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

# 14
# sum of subarray
# class Solution:
#     def subarraySum(self, arr):
#         # code here 
#         sum=0
#         n=len(arr)
#         i=0
#         for i in range(0,n):
#             sum+=arr[i]*(i+1)*(n-i)
#             i+=1
#         return sum

# 15
# You are given a String S, you need to print its characters at even indices(index starts at 0).
# s=input("Enter strring")
# print(s[::2])  
# 16
#  Capacity To Ship Packages Within D Days ( leetcode 1011)
# class Solution:
#     def shipWithinDays(self, weights: List[int], days: int) -> int:
#         l , r = max(weights),sum(weights)
#         res=r

#         def canShip(cap):
#             ships, currCap = 1, cap
#             for w in weights:
#                 if currCap - w < 0:
#                     ships += 1
#                     currCap=cap
#                 currCap -= w
#             return ships <= days
        
#         while l <= r:
#             cap = (l + r) // 2
#             if canShip(cap):
#                 res = min(res,cap)
#                 r = cap-1
#             else: 
#                 l = cap + 1
#         return res        

# 17
#  Check if a String Is an Acronym of Words (leetcode 2828)
# class Solution:
#     def isAcronym(self, words: List[str], s: str) -> bool:
#         if not len(words)==len(s) : return False
#         i=0
#         for word in words:
#             if not (word.startswith(s[i])):
#                 return False
#             i+=1
#         return True

# 18 Sort vovel in string
# class Solution(object):
#     def sortVowels(self, s):
#         vowels = []

#         s_list = list(s)

#         for i in s_list:
#             if i in "AEIOUaeiou":
#                 vowels.append(i)
        
#         if vowels == []:
#             return s

#         vowels.sort()

#         count = 0

#         for j in range(len(s)):
#             if s_list[j] in "AEIOUaeiou":
#                 s_list[j] = vowels[count]
#                 count += 1
        
#         return "".join(s_list)

# 19
# Digit freq score (leetcode)
# class Solution:
#     def digitFrequencyScore(self, n: int) -> int:
#         digits = str(n)
#         freq = {}
#         for ds in digits:
#             if ds in freq:
#                 freq[ds] += 1
#             else:
#                 freq[ds] = 1
#         total_score = 0
#         for ds, count in freq.items():
#             total_score += int(ds) * count
#         return total_score

# 20 Kth Missing Positive Number
# class Solution:
#     def findKthPositive(self, arr: List[int], k: int) -> int:
        
#         a,i,l=1,0,len(arr)
#         count = 0
        
#         while count < k and i < l:
#             if not (arr[i]==a):
#                 count += 1
                
#             else:
#                 i += 1
#             a+=1
        
#         if count < k:
#             return a + (k-count) - 1

#         return a-1


# 21 Trim trailing vowels
# class Solution:
#     def trimTrailingVowels(self, s: str) -> str:
#         vowels=['a','e','i','o','u']
#         return s.rstrip("".join(vowels))

# 22 Index of an extra element 
# class Solution:
#     def findExtra(self,a,b):
#         #add code here
#         extra = sum(arr1) - sum(arr2)
#         return arr1.index(extra)

# 22 Max sum subarray of size k
# class Solution:
#     def maxSubarraySum(self, arr, k):
#         # code here 
#         l=0
#         csum=0
#         ans=0
#         n=len(arr)
#         for r in range(n):
#             csum+=arr[r]
#             while r-l+1>k:
#                 csum -= arr[l]
#                 l+=1
#             ans = max(ans, csum)
#         return ans

# 23  Percentage of Letter in String ( leetcode 2278)
# class Solution:
#     def percentageLetter(self, s: str, letter: str) -> int:
#         count = s.count(letter)
#         percentage = (count * 100 ) // len(s) 
        
#         return int(percentage)

# 24 Jewels and Stones (leetcode 771)
# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         count = 0
#         for stone in stones:
#             if stone in jewels:
#                 count += 1
#         return count

# 25 Decode XORed Array
# class Solution:
#     def decode(self, encoded: List[int], first: int) -> List[int]:
#         i=0
#         arr = [0] * (len(encoded) + 1)
#         arr[0]=first
#         for num in encoded:
#             arr[i+1] = encoded[i] ^ arr[i]
#             i += 1
#         return arr

# 26 Partition Array According to Given Pivot
# class Solution:
#     def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
#         arr1 = []
#         same = []
#         arr2 = []

#         for num in nums:
#             if num < pivot:
#                 arr1.append(num)
#             elif num == pivot:
#                 same.append(num)
#             else:
#                 arr2.append(num)

#         res = arr1+same+arr2
#         return res

# 27 How Many Numbers Are Smaller Than the Current Number (leetcode 1365)
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         arr = nums.copy()
#         arr.sort()
        
#         res = []
#         for num in nums:
#             res.append(arr.index(num))
#         return res

# 28 check the balanced string
# class Solution:
#     def isBalanced(self, num: str) -> bool:
#         even=[]
#         odd=[]
#         i = 0
#         for nums in num:
#             if (i % 2 == 0):
#                 even.append(int(nums)) 
#             else:
#                 odd.append(int(nums))
#             i+=1
#         if(sum(even) == sum(odd)):
#             return True
#         else:
#             return False

# 29
# class Solution:
#     def countTriplet(self, arr):
#         setarr = set(arr)
#         count = 0
#         l = len(arr)

#         for i in range(l - 1):
#             for j in range(i + 1, l):
#                 if (arr[i] + arr[j]) in setarr:
#                     count += 1

#         return count

# 
class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        dig = [int(digit) for digit in str(n)]
        sq = [x**2 for x in dig]

        if ( sum(sq) - sum(dig) >= 50):
            return True
        else:
            return False