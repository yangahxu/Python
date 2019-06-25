import time
qs=input('小精灵：您好，欢迎古灵阁，请问您需要帮助吗？需要or不需要？')
#回答需要
if qs=='需要':
   #选择服务 
   qs2=int(input('小精灵：请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询'))
   #服务类型 
   if qs2==1:
        print('小精灵推荐你去存取款窗')
   elif qs2==2:
    #提示货币兑换
        print('小精灵：金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币')
        time.sleep(2)
        #计算兑换金额
        qs3=int(input('小精灵：请问您需要兑换多少金加隆呢？请输入金额'))
        print('小精灵：好的，我知道了，您需要兑换'+str(qs3)+'金加隆。')
        time.sleep(1)
        money=str(qs3*51.3)
        print('那么，您需要付给我'+money+'人民币')
   elif qs2==3:
        print('小精灵推荐你去咨询窗口')
   else:
        print('输入错误，请重新运行')

#回答不需要
elif qs=='不需要':
    print('好的，再见')
else:
    print('输入错误，请重新运行')

else