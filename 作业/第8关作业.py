#作业1-合并列表
list1 = [91, 95, 97, 99]
list2 = [92, 93, 96, 98] 

list3 = list1 + list2

print(list3)
list3.sort()#升序排列
print(list3)

#作业2
s = 0
for i in list3:
    s = s + i
average = s / 8
print(' 大家的平均分是%d ' % (average))