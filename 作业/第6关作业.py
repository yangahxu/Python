# while True:

#     a = input('小a,你认罪吗？输入认罪或不认：')
#     b = input('小b,你认罪嘛？输入认罪或不认：')
#     if a == '认罪' and b == '认罪':
#         print('两人各判10年')
#     elif a == '不认' and b == '不认':
#         print('各判3年')
#         break
#     else:
#         print('认罪的人判1年，不认的判20年')
#         list=[]
#         list.append(a)
#         list.append(b)
#         if list[0] == '不认':
#             print('小a喜提20年，小b大吉大利得1年')
#         else:
#             print('小b喜提20年，小a大吉大利得1年')
        
n = 0
list_answer = []
while True:
    n += 1
    a = input('A，你认罪吗？请回答认罪或者不认：')
    b = input('B，你认罪吗？请回答认罪或者不认：')
    list_answer.append([a,b])  # 用列表嵌套的方式来存放实验者的选择，也可用元组或字典
    if a == '认罪' and b == '认罪':
        print('两人都得判10年，唉')
    elif a == '不认' and b == '认罪':
        print('A判20年，B判1年，唉')
    elif a == '认罪' and b == '不认':
        print('A判1年，B判20年')
    else:
        print('都判3年，太棒了')
        break
print('第' + str(n) + '对实验者选了最优解。')
for i in range(n):
    # 注意数据类型的转换，以及计数起点的不同（0和1）
    print('第' + str(i+1) + '对实验者的选择是：' + str(list_answer[i]))
        