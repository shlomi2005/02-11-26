# exersice 1

# def welcome(name):
#     message = "Welcome " + name
#     return message


# result = welcome("Dana")
# print(welcome("Dana"))
# print(result)
'''
בשורה האחרונה תתקבל שגיאה NameError, כי
המשתנה message הוגדר בתוך הפונקציה welcome,
ולכן הוא מוכר רק בתוכה. מחוץ לפונקציה הוא לא קיים.
'''
# התיקון לפונקציה כבר בקוד !


# exersice 2

# x = "global"


# def first():
#     x = "local in first"
#     print("1:", x)


# def second():
#     print("2:", x)


# first()
# second()
# print("3:", x)

# # תוצאה
# 1: local in first
# 2: global
# 3: global


# exersice 3

# count = 0


# def add_one():
#     count = count + 1


# add_one()

'''תתקבל שגיאה UnboundLocalError
 בתוך הפונקציה יש שורה count = ...
 ולכן Python מחליטה שcount הוא משתנה מקומי של הפונקציה
 ולא הcount שבחוץ
 כשהשורה מנסה לחשב count + 1 ל-count
 המקומי עוד אין ערך, ולכן 
 נוצרת שגיאה'''


count = 0


def add_one(count):
    return count + 1


count = add_one(count)
print(count)
