#作业1
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
#作业2
# q = 0        
# box = []
# while True:
#     q = q + 1
#     a = input('小A，你认不认罪？')
#     b = input('小B，你认不认罪？')
#     box.append([a,b])
#     print(box)
#     print(q)
#     if a == '认罪' and b == '认罪':
#         print('两人都认罪，则各判10年')
#     elif a == '不认罪' and b == '认罪':
#         print('小A判20年,小B判1年')
#     elif  a == '认罪' and b == '不认罪':
#         print('小A判1年,小B判20年')
#     else:
#         print('两人都抵赖，各判3年')
#         break
# print('第'+str(q)+'组是最优选择')
# print('每组的结果如下:')
# for i in range(q):
    
#     print('第'+str(i+1)+'的结果为'+str(box[i]))

#作业3

# movies = {
# '妖猫传':['黄轩','染谷将太'],
# '无问西东':['章子怡','王力宏','祖峰'],
# '超时空同居':['雷佳音','佟丽娅'],
# }
# # name = input('请输入演员名称：')
# # if name in movies['妖猫传']:
# #     print(name+'出演了电影'+str(movies['妖猫传']))
# for movie in movies:#movies的键'妖猫传'，‘妖猫传’=movie，so,movies['妖猫传']=movies[movie]=actors;
#     print(movie)
#     actors=movies[movie]
#     print(actors) 
