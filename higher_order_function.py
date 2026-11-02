# exercise 1
# def double(n):
#     return n * 2


# def apply_to_all(numbers, action):

#     result = []
#     for n in numbers:
#         result.append(action(n))
#     return result


# print(apply_to_all([1, 2, 3], double))
# print(apply_to_all([1, 2, 3], lambda n: n * n))
# print(apply_to_all([1.6, 2.4], round))


# exercise 2

# prices = [20, 75, 120, 45, 90]

# expensive = list(filter(lambda p: p > 50, prices))
# print(expensive)

# plus_ten = list(map(lambda p: p+10, expensive))
# print(plus_ten)


# exercise 3
# words = ["banana", "fig", "cherry", "kiwi"]
# students = [("Dana", 92), ("Avi", 78), ("Noa", 85)]
# print(sorted(words, key=len))
# print(max(words, key=len))

# by_grade = sorted(students, key=lambda s: s[1], reverse=True)
# for s in by_grade:
#     print(s[0])
