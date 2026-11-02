# exercise 1

# def make_greeting(name, greeting="Hello", punct="!"):
#     return greeting + ", " + name + punct


# print(make_greeting("Dana"))
# print(make_greeting("Avi", "Good morning"))
# print(make_greeting("Noa", punct="?"))

# exercise 2


# def average(*numbers):
#     if not numbers:
#         raise ValueError("need at least one number")
#     return sum(numbers)/len(numbers)


# print(average(80, 90))
# print(average(70, 80, 90, 100))
# try:
#     average()
# except ValueError as error:
#     print("error:", error)


# exercise 3
def format_profile(name, **details):
    result = []
    for k, v in details.items():
        result.append(f"{k}={v}")
    return f"{name}: {",".join(result)}"


print(format_profile("dana", age=25, city="haifa"))
print(format_profile("avi"))
