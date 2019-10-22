# name=input('请给猫头鹰起名字：')
# print('哈利·波特的猫头鹰叫做'+name)

# qt=int(input('你今天吃了几个巧克力？'))

# if qt>10:
#     print('你要给我100块')
# else:
#     print('我给你100块')
# print('程序结束')

#古灵阁换钱
import time
time.sleep(1)
need=input('小精灵：您好，欢迎古灵阁，请问您需要帮助吗？需要or不需要？')
if need == '需要':
    need=input('小精灵：请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询')
    if need=='1':
        print('小精灵会推荐你去存取款窗口')
    elif need=='2':
        print('小精灵：金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币')
        need=int(input('小精灵：请问您需要兑换多少金加隆呢？'))

        print('小精灵：好的，我知道了，您需要兑换'+str(need)+'金加隆。')
        money=need*51.3
        m2='%.2f'%money
        print('小精灵：那么，您需要付给我'+m2+'人民币。')
    elif need=='3':
        print('小精灵会推荐你去咨询窗口')

elif need == '不需要':
    print('好的，再见！')
else:
    print('输入错误，程序结束。')


#保留两位消数
# money=28*51.3
# m2='%.2f'%money

# print(m2)