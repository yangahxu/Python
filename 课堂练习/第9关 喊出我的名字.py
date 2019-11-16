# #def()函数
# #第一个函数
# def pika1():
#     print('我最喜爱的神奇宝贝是皮卡丘')

# #第二个函数
# def pika2(name):
#     print('我最喜爱的神奇宝贝是'+name)
    
# #第三个函数
# def pika3(name,person):
#     print('我最喜爱的神奇宝贝是'+name)
#     print('我最喜爱的驯兽师是'+person)

# def pika2(name):
#     print('我最喜爱的神奇宝贝是'+name)
# pika2('皮卡丘')  #调用函数，输入函数名pika()并输入参数'皮卡丘'
# pika2('喷火龙')  #调用函数，输入函数名pika()并输入参数'喷火龙'

# pika3('可达鸭',('小霞'))

# #打印圣诞树

# def tree(Height):
#     print('Merry Christmas!')
#     for i in range(Height):
#         print((Height-i)*2*' '+'o'+ i*'~x~o')
#         print(((Height-i)*2-1)*' '+(i*2+1)*'/'+'|'+(i*2+1)*'\\')
# tree(4)
# tree(8)

# #位置参数
# def  menu(appetizer,course):#这里的'话梅花生'和'牛肉拉面'是对应参数appetizer和course的位置顺序传递的，所以被叫作【位置参数】
#     print('一份开胃菜：'+appetizer)
#     print('一份主食：'+course+'\n')
# #还记得转义字符\n吧，表示换行
# menu('牛肉拉面','话梅花生')
# menu('话梅花生','牛肉拉面')
# #如果采用下面这种形式传递，就不需要理会参数位置
# menu(course='牛肉拉面',appetizer='话梅花生')

# #默认参数

# def  menu(appetizer,course,dessert='绿豆沙'):#默认参数必须放在位置参数之后
#     print('一份开胃菜：'+appetizer)
#     print('一份主食：'+course)
#     print('一份甜品：'+dessert)
# menu('话梅花生','牛肉拉面')
# #因为已经默认将'绿豆沙'传递给dessert，调用时无须再传递。


# def menu(appetizer,course,dessert='绿豆沙'):
#     print('一份开胃菜：'+appetizer)
#     print('一份主食：'+course)
#     print('一份甜品：'+dessert)
# menu('话梅花生','牛肉拉面')
# menu('话梅花生','牛肉拉面','银耳羹')#改变默认参数
# #银耳羹对应参数dessert

# #不定长参数，它的格式比较特殊，是一个星号*加上参数名。
# def menu(*barbeque):
#     print(barbeque)
# menu('烤鸡翅','烤茄子','烤玉米')
# #这几个值都会传递给参数barbeque，生成元组

# order=('烤鸡翅','烤茄子','烤玉米')#生成元组，传入参数
# #元组的长度没有限制
# def menu(*barbeque):
#     print(barbeque)
# menu(*order)

# #遍历不定长参数，for循环
# def menu(appetizer,course,*barbeque,dessert='绿豆沙'):#默认参数也需要放在不定长参数的后面
#     print('一份开胃菜：'+appetizer)
#     print('一份主食：'+course)
#     print('一份甜品：'+dessert)
#     for i in barbeque:
#         print('一份烤串：'+i)
# menu('柠檬洋芋','米饭','小肉串','腰子','油腰子','火腿肠')

# #函数嵌套
# def face(name):
#     return name + '的脸蛋'
# def body(name):
#     return name + '的身体'
# print('我的梦中情人：'+face('李若彤')+'+'+body('林志玲'))

# #多次调用函数
# def face(name):
#     return name + '的脸蛋'
# def body(name):
#     return name + '的身体'
# def main(face_name,body_name):
#     return '我的梦中情人' + face(face_name) + '+' + body(body_name)
# print(main('李若彤','林志玲'))
# print(main('高希霸','嘉辉'))

# #没有return语句返回None值
# #第一个函数
# def fun():
#     a ='I am coding'
# print(fun())
# #第二个函数
# def fun():
#     a='I am coding'
#     return a
# print(fun())

# #return还有一个“副作用”：一旦函数内部遇到return语句，就会停止执行并返回结果。
# def fun():
#     return 'I am coding.'
#     return 'I am not coding.'
# print(fun())

# #打印较大值
# def large(number1,number2):
#     if number1 > number2:
#         return number1
#     elif number1 == number2:
#         return '一样大哦'
#     else:
#         return number2
# print(large(99**2,8888))

# #变量作用域
# x=99   #全局变量x  
# def num():
#     x=88 #局部变量x 
#     print(x)
    
# num() #结果88
# #打印局部变量x

# print(x) #结果99
# #打印全局变量x

qty = 108
def egg():
    print(qty)
egg()

def egg():    
    global quantity
    quantity = 108
egg()
print(quantity)

m1 = 3
def myfunction():
    print(m1)
    m2 = 8
    print(m2)

myfunction()