#练习1
stonenum=int(input("偷回来几个石头？"))

if stonenum>=4:
    print("获得了打败灭霸的力量，反杀稳了")
elif 0<stonenum<4:
    print('可以全员出动，殊死一搏')
else:
    print('没办法了，只能尝试呼叫惊奇队长')
print('程序结束')

#练习2
gongzi=int(input('美国队长的工资是多少：'))

if gongzi<=500:
    print('欢迎进入史塔克穷人帮前三名')
    if 100<gongzi<=500:
        print('请找弗瑞队长加薪')
    else:
        print('恭喜您荣获“美元队长”称号！')
elif 500<gongzi<=1000:
    print('祝贺您至少可以温饱了。')
else:
    print('经济危机都难不倒您！')
    if 1000<=gongzi<=20000:
        print('您快比钢铁侠有钱了！')
    else:
        print('您是不是来自于瓦坎达国？')
print('程序结束')