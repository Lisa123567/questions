# #Merging sort ##O(n*log(n))##
# def bubbleSort(alist):
#     print("Splitting ", alist)
#     if len(alist) > 1:
#         mid = len(alist) // 2
#         lethal = alist[:mid]
#         rightful = alist[mid:]
#
#         bubbleSort(lethal)
#         bubbleSort(rightful)
#
#         i = 0
#         j = 0
#         k = 0
#         while i < len(lethal) and j < len(rightful):
#             if lethal[i] < rightful[j]:
#                 alist[k] = lethal[i]
#                 i = i + 1
#             else:
#                 alist[k] = rightful[j]
#                 j = j + 1
#             k = k + 1
#
#         while i < len(lethal):
#             alist[k] = lethal[i]
#             i = i + 1
#             k = k + 1
#
#         while j < len(rightful):
#             alist[k] = rightful[j]
#             j = j + 1
#             k = k + 1
#     print("Merging ", alist)
# ###2
# def bubbleSort(alist):
#     for passnum in range(len(alist) - 1, 0, -1):
#         for i in range(passnum):
#             if alist[i] > alist[i + 1]:
#                 temp = alist[i]
#                 alist[i] = alist[i + 1]
#                 alist[i + 1] = temp
# # for both:
# mylist = [54, 26, 93, 17, 77, 23,-5,78,31, 44, 55, 20]
# bubbleSort(mylist)
# print(mylist)
#
# # O(n) - matrix if it magic-square sum(row)= sum(Leftdiagonal)= sum(Leftdiagonal) = sum(colum)
# def m(matrix):
#     vSum = 0
#     hSum = 0
#     l1Sum = 0
#     l2Sum = 0
#     for i, v in enumerate(matrix):
#         vSum += matrix[i][0]
#         hSum += matrix[0][i]
#         l1Sum += matrix[i][i]
#         l2Sum += matrix[i][len(matrix) - i - 1]
#
#     if vSum == hSum and vSum == l1Sum and vSum == l2Sum:
#         return True
#     return False
#
# matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],[1, 1, 1, 1]]
# #matrix = [[1, 2, 3, 4], [1, 2, 3, 5], [1, 1, 1, 1]]
# print(m(matrix))
# 4 - function get and sorted list and number,checks if there are 2 elements
# in the list whose sum is equal to the number.
# Without repeating an element twice   # O(2n)
def f(sorted_arr, sum):
    sec_nums = {}
    for num in sorted_arr:
        if not sec_nums.get(sum - num):
            sec_nums[sum - num] = 1
        else:
            sec_nums[sum - num] = +1
    for sec_num in sorted_arr:
        sec_exists = sec_nums.get(sec_num)
        if sec_num == sum - sec_num and sec_exists and sec_exists > 1:
            print(sec_num)
            return True
        if sec_num != sum - sec_num and sec_exists:
            print(sec_num)
            return True
    return False


arr = [2, 2, 4, 6, -2]
n = 6
print(f(arr, n))