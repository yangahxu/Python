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
average = s / len(list3)
print(' 大家的平均分是%s ' % (average))
print(len(list3))#显示列表长度

#方法一:提取小于平均分的数字,int(average),直接使用average结果不符,95未排除;
selected = [x for x in list3 if x < average]
print(selected)

#方法二:循环
list4 = []
for score  in list3:
    if score < int(average):
        list4.append(score)
print('低于平均分的有:{}'.format(list4))

#方法三:numpy
a = int(average)
import numpy as np
print(int(np.mean(list3)))#平均值的方法
socres3 = np.array(list3)
print(' 低于平均成绩的有：{}'.format(socres3[socres3 < a]))
print(socres3[socres3 < a])