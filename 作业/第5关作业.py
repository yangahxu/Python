# #第一种 for
# for i in [1,2,3,5,6,7]:
#     print(i)
# #第二种 for
# for i in range (1,8):
#     if i !=4:
#         print(i)
#While用法一
# i = 1
# while i !=4:
#     print(i)
#     i = i+1
# while 4 <= i < 7:
#     i = i+1
#     print(i)
#while用法二：
# n = 0
# while n < 7:
#     n = n+1
#     if n != 4:  # 当num != 4，执行打印语句；等于4时不打印。
#         print(n)
# students = ['小明','小红','小刚']
# for i in range (3):
#     print(students)
#     st1 = students.pop(0)
#     print(students)
#     print(st1)
#     students.append(st1)
#     print(students)

#答案
# students = ['小明','小红','小刚']
# for i in range(3):
#     student1 = students.pop(0)  # 运用pop()函数，同时完成提取和删除。
#     students.append(student1)  # 将移除的student1安排到最后一个座位。
#     print(students)

# students = ['小明','小红','小刚']
# for i in ['小明','小红','小刚']:
#     print(students)
#     del students[0]
#     students.append(i)


# students = ['小明','小红','小刚']
# while students[0] == students[0]:
    
#     students.append(students[0])
#     del students[0]
#     print(students)

#用while处理
students = ['小明','小红','小刚']
a = 1
while a < 4:
    print(students)
    students.append(students[0])
    del students[0]
    a =a+1
print('游戏结束')

