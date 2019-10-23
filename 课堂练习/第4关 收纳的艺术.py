# students = ['党志文', '浦欣然', '罗鸿朗', '姜信然', '居俊德', '宿鸿福', '张成和', '林景辉', '戴英华', '马鸿宝', '郑翰音', '厉和煦', '钟英纵', '卢信然', '任正真', '翟彭勃', '蒋华清', '双英朗', '金文柏', '饶永思', '堵宏盛', '濮嘉澍', '戈睿慈', '邰子默', '于斯年', '扈元驹', '厍良工', '甘锐泽', '姚兴怀', '殳英杰', '吴鸿福', '王永年', '宫锐泽', '黎兴发', '朱乐贤', '关乐童', '养永寿', '养承嗣', '贾康成', '韩修齐', '彭凯凯', '白天干', '瞿学义', '那同济', '衡星文', '公兴怀', '宫嘉熙', '牧乐邦', '温彭祖', '桂永怡']
# for i in students:
#     print(i+'在不在？')

# list1=['小明',18,1.70]
# print(list1)
# print(list1[0])

# list2 = [5,6,7,8,9]
# print(list2[:])
# # 打印出[5,6,7,8,9]
# print(list2[2:])
# # 打印出[7,8.9]
# print(list2[:2])
# # 打印出[5,6]
# print(list2[1:3])
# #打印出[6,7]
# print(list2[2:4])    
# #打印出[7,8]

#冒号左边空，就要从偏移量为0的元素开始取；右边空，就要取到列表的最后一个元素。
# 后半句：冒号左边数字对应的元素要拿，右边的不动

#练习
# students = ['小明','小红','小刚']
# print(students[:2])
# print(students[0])

# 请运行以下代码：报错后，可读一下报错信息，然后将第6行注释掉再运行。
list3 = [1,2]
list3.append(3)
print(list3)
#list3.append(4,5)
list3.append([4,5])
print(list3)

# students = ['小明','小红','小刚']
# students.append('小美')
# print(students)
# del students[1]
# print(students)

# students = ['小明','小红','小刚']
# scores = {'小明':95,'小红':90,'小刚':90}
# print(len(students))
# print(len(scores))
# print(scores['小明'])
# print(scores['小红'])

# album = {'周杰伦':'七里香','王力宏':'心中的日月'}
# del album['周杰伦']
# print(album)
# album['周杰伦'] = '十一月的萧邦'
# print(album)
# print(album['周杰伦'])

#修改成绩
# scores = {'小明':95,'小红':90,'小刚':90}
# del scores['小刚']
# print(scores)
# scores['小刚']=92
# print(scores)
# scores['小美']=85
# print(scores)


# students1 = ['小明','小红','小刚']
# students2 = ['小刚','小明','小红']
# print(students1 == students2)

# scores1 = {'小明':95,'小红':90,'小刚':100}
# scores2 = {'小刚':100,'小明':95,'小红':90}
# print(scores1 == scores2)

# list1 = ['小明','小红','小刚','小美']
# list1[1] = '小蓝'
# print(list1)

# dict1 = {'小明':'男'}
# dict1['小明'] = '女'
# print(dict1)

#列表嵌套列表
# students = [['小明','小红','小刚','小美'],['小强','小兰','小伟','小芳']]
# print(students[1][1])

# #字典嵌套字典
# scores = {
#     '第一组':{'小明':95,'小红':90,'小刚':100,'小美':85},
#     '第二组':{'小强':99,'小兰':89,'小伟':93,'小芳':88}
#     }
# print(scores['第一组']['小刚'])


# students = {
#     '第一组':['小明','小红','小刚','小美'],
#     '第二组':['小强','小兰','小伟','小芳']
#     }
# scores = [
#     {'小明':95,'小红':90,'小刚':100,'小美':85},
#     {'小强':99,'小兰':89,'小伟':93,'小芳':88}
#     ]

# print(students['第一组'][2])  
# print(scores[0]['小刚'])