#自定属性，人工PK
# import time

# print('【玩家】\n血量：100 \n攻击：50')  # 自定义玩家角色的血量和攻击
# print('------------------------') 
# time.sleep(1.5)
# print('【敌人】\n血量：100 \n攻击：30')
# print('------------------------')   # 自定义敌人角色的血量和攻击
# time.sleep(1.5)
# print('你发起了攻击，【敌人】剩余血量50')  # 人工计算敌人血量：100-50=50
# print('敌人向你发起了攻击，【玩家】剩余血量70')
# print('------------------------')   # 人工计算玩家血量：100-30=70
# time.sleep(1.5)
# print('你发起了攻击，【敌人】剩余血量0')  # 双方同时攻击，若血量出现小于等于0，游戏结束
# print('敌人向你发起了攻击，【玩家】剩余血量40')
# print('------------------------') 
# time.sleep(1.5)
# print('敌人死翘翘了，你赢了！') # 打印结果

# 随机属性和自动战斗
import time,random
a = 0
player_victory = 0
enemy_victory = 0
for i in range(3):
    time.sleep(1.5)
    a += 1
    print('\n---------------现在是第'+str(a)+'局-----------------')
    player_life = random.randint(100,150)
    player_attack = random.randint(30,50)
    enemy_life = random.randint(100,150)
    enemy_attack = random.randint(30,50)
    print('【玩家】\n血量：%s\n攻击：%s' % (player_life,player_attack))  # 自定义玩家角色的血量和攻击
    print('------------------------') 
    time.sleep(1.5)
    print('【敌人】\n血量：%s\n攻击：%s' % (enemy_life,enemy_attack))
    print('------------------------')   # 自定义敌人角色的血量和攻击
    time.sleep(1.5)


    while player_life > 0 and enemy_life > 0:
        player_life = player_life - enemy_attack
        enemy_life = enemy_life - player_attack
        print('你发起了攻击，【敌人】剩余血量%s' % (enemy_life))  # 人工计算敌人血量：100-50=50
        print('敌人向你发起了攻击，【玩家】剩余血量%s' % (player_life))
        print('------------------------')   # 人工计算玩家血量：100-30=70
        time.sleep(1.5)
    if player_life > 0 and enemy_life <= 0:
        player_victory += 1
        print('敌人死翘翘了，你赢了')
    elif player_life <= 0 and enemy_life > 0:
        enemy_victory += 1
        print('悲催，敌人把你干掉了！')
    else:
        print('哎呀，你和敌人同归于尽了！')
    print('当前比分\n【玩家：%s--敌人：%s】'% (player_victory,enemy_victory))
if player_victory > enemy_victory :
    time.sleep(1)
    print('【最终结果：你赢了！】')
elif enemy_victory > player_victory:
    print('【最终结果：你输了！】')
else: 
    print('【最终结果：平局！】')


# lucky = 8
# print('我的幸运数字是%d' % lucky)
# print('我的幸运数字是%d' % 8)
# print('我的幸运数字是%s' % '小龙女的生日816')
# print('我的幸运数字是%d和%d' % (8,16))

# print('我的幸运数字是%d，而且我不知道%d' % (8,16))  #8以整数展示
# print('我的幸运数字是%s' % 8)  #8以字符串展示
# print(8) #整数8与字符串'8'打印出来的结果是一样的
# print('8')


