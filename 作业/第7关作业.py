#while+break
import time,random
a = 0
player_victory = 0
enemy_victory = 0
while True:
    
    for i in range(3):
        
        time.sleep(1.5)
        a += 1
        print('\n---------------现在是第'+str(a)+'局-----------------')
        player_life = random.randint(100,150)
        player_attack = random.randint(30,50)
        enemy_life = random.randint(100,150)
        enemy_attack = random.randint(30,50)
        print('【玩家】\n血量：%s\n攻击：%s' % (player_life,player_attack))  
        print('------------------------') 
        time.sleep(1.5)
        print('【敌人】\n血量：%s\n攻击：%s' % (enemy_life,enemy_attack))
        print('------------------------')   
        
        time.sleep(1.5)
        while player_life > 0 and enemy_life > 0:
            player_life = player_life - enemy_attack
            enemy_life = enemy_life - player_attack
            print('你发起了攻击，【敌人】剩余血量%s' % (enemy_life))  
            print('敌人向你发起了攻击，【玩家】剩余血量%s' % (player_life))
            print('------------------------')   
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
    time.sleep(1.5)
    if player_victory > enemy_victory :
        print('【最终结果：你赢了！】')
    elif enemy_victory > player_victory:
        print('【最终结果：你输了！】')
    else: 
        print('【最终结果：平局！】')
    print('-----------------------------')
    again = input('是否再来一局？输入是或不是')
    if again == '是':
        a = 0
        continue
    else:
        break
print('游戏结束，欢迎再来！')

#while+变量
import time,random
again = '是'
a = 0
player_victory = 0
enemy_victory = 0
while again == '是':
    
    for i in range(3):
        
        time.sleep(1.5)
        a += 1
        print('\n---------------现在是第'+str(a)+'局-----------------')
        player_life = random.randint(100,150)
        player_attack = random.randint(30,50)
        enemy_life = random.randint(100,150)
        enemy_attack = random.randint(30,50)
        print('【玩家】\n血量：%s\n攻击：%s' % (player_life,player_attack))  
        print('------------------------') 
        time.sleep(1.5)
        print('【敌人】\n血量：%s\n攻击：%s' % (enemy_life,enemy_attack))
        print('------------------------')   
        
        time.sleep(1.5)
        while player_life > 0 and enemy_life > 0:
            player_life = player_life - enemy_attack
            enemy_life = enemy_life - player_attack
            print('你发起了攻击，【敌人】剩余血量%s' % (enemy_life))  
            print('敌人向你发起了攻击，【玩家】剩余血量%s' % (player_life))
            print('------------------------')   
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
    time.sleep(1.5)
    if player_victory > enemy_victory :
        print('【最终结果：你赢了！】')
    elif enemy_victory > player_victory:
        print('【最终结果：你输了！】')
    else: 
        print('【最终结果：平局！】')
    print('-----------------------------')
    a = 0
    again = input('是否再来一局？输入是或不是')
print('游戏结束，欢迎再来！')

#新格式化字符串方式：
import time,random
a = 0
player_victory = 0
enemy_victory = 0
while True:
    
    for i in range(3):
        
        time.sleep(1.5)
        a += 1
        print('\n---------------现在是第{}局-----------------'.format(a))
        player_life = random.randint(100,150)
        player_attack = random.randint(30,50)
        enemy_life = random.randint(100,150)
        enemy_attack = random.randint(30,50)
        print('【玩家】\n血量：{}\n攻击：{}'.format(player_life,player_attack))  
        print('------------------------') 
        time.sleep(1.5)
        print('【敌人】\n血量：{}\n攻击：{}'.format(enemy_life,enemy_attack))
        print('------------------------')   
        
        time.sleep(1.5)
        while player_life > 0 and enemy_life > 0:
            player_life = player_life - enemy_attack
            enemy_life = enemy_life - player_attack
            print('你发起了攻击，【敌人】剩余血量{}'.format(enemy_life))  
            print('敌人向你发起了攻击，【玩家】剩余血量{}'.format(player_life))
            print('------------------------')   
            time.sleep(1.5)
        if player_life > 0 and enemy_life <= 0:
            player_victory += 1
            print('敌人死翘翘了，你赢了')
        elif player_life <= 0 and enemy_life > 0:
            enemy_victory += 1
            print('悲催，敌人把你干掉了！')
        else:
            print('哎呀，你和敌人同归于尽了！')
        print('当前比分\n【玩家：{}--敌人：{}】'.format(player_victory,enemy_victory))
    time.sleep(1.5)
    if player_victory > enemy_victory :
        print('【最终结果：你赢了！】')
    elif enemy_victory > player_victory:
        print('【最终结果：你输了！】')
    else: 
        print('【最终结果：平局！】')
    print('-----------------------------')
    again = input('是否再来一局？输入是或不是')
    if again == '是':
        a = 0
        continue
    else:
        break
print('游戏结束，欢迎再来！')