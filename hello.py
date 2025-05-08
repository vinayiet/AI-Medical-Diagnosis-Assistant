from collections import defaultdict

# arr = [43, 20, 35, 25, 15]

# # selection sort
# def minimum(arr):
#     min_num = arr[0]
#     index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < min_num:
#             min_num = arr[i]
#             index = i
#     return min_num, i

# # def selection_sort(arr):
# #     i = 0
# #     min
# print(minimum(arr))


# 1 -> I 
# 2 -> II
# 3 -> III
# 4 -> IV
# 5 -> V


# def selection_sort(arr):
#     # the array iteration would be n - 2
#     for i in range(len(arr) - 2):
#         minimum_index = i
        
#         for j in range(i, len(arr) - 2):
#             if arr[j] < arr[minimum_index]:
#                 # find the index where the minimum element has been found
#                 minimum_index = j
#         # swapped the number 
#         temp = arr[minimum_index]
#         arr[minimum_index] = arr[i]
#         arr[i] = temp

# def bubble_sort(arr):
#     for i in range(len(arr) - 1):
#         for j in range(len(arr) - 1 - i):
#             if arr[j] > arr[j + 1]:
#                 temp = arr[j]
#                 arr[j] = arr[j + 1]
#                 arr[j + 1] = temp

# def bubble_sort1(arr): # this is the optimised sorting where the time complexity is n for the best case 
#     for i in range(len(arr) - 1):
#         swap = 0
#         for j in range(len(arr) - 1 - i):
#             if arr[j] > arr[j + 1]:
#                 temp = arr[j]
#                 arr[j] = arr[j + 1]
#                 arr[j + 1] = temp
#                 swap = 1
#         if swap == 0:
#             break



# arr = [4 , 3, 5, 7, 1]
# # selection_sort(arr)
# bubble_sort1(arr)
# print(arr)
    
    # Example of a 2D array
# matrix = [
#         [1, 2, 3],
#         [4, 0, 6],
#         [7, 8, 9]
#     ]

    # Print the 2D array

# # record the indexes which are having 0
# row = len(matrix)
# column  = len(matrix[0])
# zero_col = set()
# zero_row = set()


# # recording the zero indexes through matrix
# for i in range(row):
#     for j in range(column):
#         if matrix[i][j] == 0:
#             zero_row.add(i)
#             zero_col.add(j)
# # setting the values 
# for i in range(row):
#     for j in range(column):
#         if i in zero_row or j in zero_col:
#             matrix[i][j] = 0

# for c in matrix:
#     print(c)


# Printing the pascals traingle
# def combination(n):
#     # [1 => (nCr), 4, 6, 4, 1]
#     ans = 1
#     res = []
#     res.append(ans)
#     for i in range(1, n):
#         ans = ans * (n - i)
#         ans = ans // i
#         res.append(ans)
#     return res

# def print_pascal(n):
#     final_ans = []
#     for i in range(1, n):
#         final_ans.append(combination(i))
#     return final_ans

# print(print_pascal(7))


# Input: n = 19
# Output: true
# Explanation:
# 1 2 + 9 2 = 82 => 
# 8 2 + 2 2 = 68
# 6 2 + 8 2 = 100
# 1 2 + 0 2 + 0 2 = 1
# n = 99

# while n > 0:
#     ones_place = n % 10
#     tens_place = (n // 10) % 10

#     print("Ones place digit:", ones_place)
#     print("Tens place digit:", tens_place)
#     break  # Exit the loop after processing the digits
# nums = [9,1,4,7,3,-1,0,5,8,-1,6]
# sorted_arr = sorted(nums)
# print(sorted_arr)
# count = 1
# for i in range(len(sorted_arr) - 1):
#     if sorted_arr[i] + 1 != sorted_arr[i + 1]:
#         continue
#     else:
#         count += 1
# print(count)


# s = 'abcb'
# count = 1
# maxCount = 1
# res = set()

# # Generate all possible subarrays
# for i in range(len(s)):
#     for j in range(i , len(s) + 1):

#         set.add(s[i])
# res


# prices = [7,1,5,3,6,4]
# maxProfit = 0
# for i in range(1, len(prices)):
#     if prices[i] > prices[i - 1]:
#         maxProfit += (prices[i] - prices[i - 1])

# print(maxProfit)


# arr = [2,4,3,3]
# seen = set()
# for i in range(len(arr)):
#     if arr[i] in seen:
#         print('True')
#     seen.add(arr[i])


# s1 = 'nagaram'
# s2 = 'anagram'

# dic = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
# for c in s1:
#     dic[c] += 1
# for d in s2:
#     dic[d] -= 1
# if any(value > 0 for value in dic.values()):
#     print("False")
# else:
#     print("True")

# dic = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
# strs = ["eat","tea","tan","ate","nat","bat"]

# anagrams = defaultdict(list)
# for word in strs:
#     sorted_word = ''.join(sorted(word))
#     anagrams[sorted_word].append(word)
# print(list(anagrams.values()))

# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, item):
#         self.stack.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         else:
#             raise IndexError("Pop from an empty stack")

#     def peek(self):
#         if not self.is_empty():
#             return self.stack[-1]
#         else:
#             raise IndexError("Peek from an empty stack")

#     def is_empty(self):
#         return len(self.stack) == 0

#     def size(self):
#         return len(self.stack)

# # Example usage:
# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# print(stack.pop())  # Output: 30
# print(stack.peek())  # Output: 20
# print(stack.is_empty())  # Output: False


# Top frequent k elements 
# arr = [1,2,1,2,1,3]

# hash = {}
# for num in arr:
#     if num in hash:
#         hash[num] += 1
#     else:
#         hash[num] = 1

# sorted_arr =sorted(hash,key = lambda x:hash[x], reverse=True)
# k = 1
# print(arr[:2])

# arr = [1,2,3,4]
# # pre product -> [1] 
# pre = [1] * len(arr)
# left_prod = 1
# for i in range(len(arr)):
#     pre[i] = left_prod
#     left_prod = left_prod * arr[i]
# print(f'This is the pre product', pre)

# post = [1] * len(arr)
# right_prod = 1
# for i in range(len(arr) - 1, -1, -1):
#     post[i] = right_prod
#     right_prod = right_prod * arr[i]

# print(f'This is the right product:', post)

# for i in range(len(pre)):
#     arr[i] = pre[i] * post[i]

# print(arr)

# [1,2,3,4]
# 24, 12, 8, 6

