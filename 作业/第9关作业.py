import random
import time
#第二部分
#用random函数在列表中随机抽奖，列表中只有3位候选者。
luckylist = ['海绵宝宝','派大星','章鱼哥']
a = random.choice(luckylist)
print('开奖倒计时',3)
time.sleep(1)
print('开奖倒计时',2)
time.sleep(1)
print('开奖倒计时',1)
time.sleep(1)

#使用三引号打印helloKitty的头像
image = '''
/\_)o<
|     \\
| O . O|
\_____/
'''
print(image)
print('恭喜'+a+'中奖！')#使用print函数打印幸运者名单