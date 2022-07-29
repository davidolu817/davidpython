# def two_sum(list_of_numbers: list, target: int) -> list:
#     for i in range(len(list_of_numbers) - 1):
#         for j in range(i + 1, len(list_of_numbers)):
#             res = list_of_numbers[i] + list_of_numbers[j]
#             if target == res:
#                 return [i, j]
#
#     return[]
#
# print(two_sum([3, 1, 5, -8], 6))


# def two_sum(list_of_numbers: list, target: int) -> list:
#     for i in range(len(list_of_numbers) - 1):
#         for j in range(i + 1, len(list_of_numbers)):
#             res = list_of_numbers[i] + list_of_numbers[j]
#             if target == res:
#                 return [i, j]
#
#     return []
#
#
# print(two_sum([6, -6, 3, 0, -8, 5, 3], 6))
#
#
# def two_sum(list_of_numbers: list, target: int) -> list:
#     map_ = {}
#     for i in range(len(list_of_numbers)):
#         complement = target - list_of_numbers[i]
#
#         if complement in map_:
#             return [map_[complement], i]
#         else:
#             map_[list_of_numbers[i]] = i
#
#     return []
#
#
# print(two_sum([1, 3, -8, 5, 3], 8))