# print(3<5)
# print(3>5)
# print('长安'=='长安')  
# print('长安'!='金陵') 

# while True:
#     print('while False')


# password = input('请输入密码：')
# if password == 'abc':
#     print('密码正确！')
# else:
#     print('密码错误！')

# if 1:
#     print('熊猫')

# print('以下数据判断结果都是【假】：')
# print(bool(False))
# print(bool(0))
# print(bool(''))
# print(bool(None))


# 请先阅读代码，然后直接运行
# a = 1
# b = -1
# print('以下是and运算')
# if a==1 and b==1:    # 【b实际上是-1】
#     print('True')
# else:
#     print('False')

# print('以下是or运算')
# if a==1 or b==1:  # 【b实际上是-1】
#     print('True')
# else:
#     print('False')


# 直接运行代码即可
# list = [1,2,3,4,5]
# a = 1
# # 做一次布尔运算，判断“a是否在列表list之中”
# print(bool(a in list))
# print(bool(a not in list))

# i = 3
# while i:
#     print('100遍')

# students = ['小明','小红','小刚']
# a = 3
# while a:
#     print(students)
#     students.append(students[0])
#     del students[0]
#     a =a-1
# print('游戏结束')
   
# for i in range(5):
#     print('明日复明日')
#     if i==3:  # 当i等于3的时候触发
#         break # 结束循环

# while True:    
#     print('上供一对童男童女')
#     t = input('孙悟空来了吗')
#     if t == '来了':
#         break
# print('孙悟空制服了鲤鱼精，陈家庄再也不用上供童男童女了')

# while True:
#     p = input('请输入小龙女结束循环：')
#     if p == '小龙女':
#         break
# print('游戏结束')

# for i in range(5):
#     print('明日复明日')
#     if i==3:  # 当i等于3的时候触发
#         continue # 回到循环开头
#     print('这句话在i等于3的时候打印不出来')

# while True:
#     q1 = input('第一问：你一生之中，在什么地方最是快乐逍遥？')
#     if q1 != '黑暗的冰窖':
#         continue
#     print('答对了，下面是第二问：')
#     q2 = input('你生平最爱之人，叫什么名字？')
#     if q2 != '梦姑':
#         continue
#     print('答对了，下面是第三问：')
#     q3 = input('你最爱的这个人相貌如何？')
#     if q3 == '不知道':
#         break
# print('都答对了，你是虚竹。')


#请你运行代码体验一下
# a = int(input('请输入一个整数:'))
# if a >= 100:
#     pass
# else:
#     print('你输入了一个小于100的数字')

# for i in range(5):
#     a = int(input('请输入0来结束循环，你有5次机会:'))
#     if a == 0:
#         print('你触发了break语句，循环结束，导致else语句不会生效。')    
#         break
# else:
#     print('5次循环你都错过了，else语句生效了。')
# i = 5
# while i:
#     a = int(input('请输入0来结束循环，你有5次机会:'))
#     i = i-1
#     if a == 0:
#         print('你触发了break语句，循环结束，导致else语句不会生效。')    
#         break
# else:
#     print('5次循环你都错过了，else语句生效了。')


# while True:
#     a = int(input('请你猜一个数字：'))
#     if a < 24:
#         print('太小了')
#         continue
#     if a > 24:
#         print('太大了')
#         continue
#     if a == 24:
#         break
# print('恭喜你，答对了')
    
# secret = 24
# while True:       
#     guess = input('你来猜猜我的秘密数字是多少:')   #输入猜测数字
#     if int(guess)==secret:  #数字对比
#         print('正确！你很棒哦。') 
#         break
#     elif int(guess)>secret:
#         print('你猜的太大了，请重新猜猜~')
#     else:
#         print('你猜的太小了，请重新猜猜~')

secret = 24
for i in range(3):
    guess = int(input('请猜一下数字：'))
    if guess == secret:
        print('答对了')
        break
    elif guess < secret:
        print('太小了')
    else:
        print('太大了')
else:
    print('失败了，游戏结束！')