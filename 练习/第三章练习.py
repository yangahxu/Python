#3-1练习
names=['yang','wang','zhang','li']
print(names[0].title())
print(names[1])
print(names[2])
print(names[-1])
#3-2练习
message='Welcome to Baoshan'
print(names[0].title()+' '+message)
print(names[1].title()+' '+message)
print(names[2].title()+' '+message)
print(names[-1].title()+' '+message)
#3-3练习
tools=['汽车','卡车','飞机']
juzi='我喜欢骑'+tools[0]+'去上班'
print(juzi)
#3-4嘉宾名单
wcnames=['tom','lilei','wanghua','yangjun']
juzi='我想邀请你们共进晚餐'
print(wcnames[0].title(),wcnames[1].title(),wcnames[2].title(),wcnames[3].title()+juzi)
#3-5 不能来的
bnlai=wcnames.pop(0)
wcnames.append('gaoli')
print('由于'+bnlai.title()+'有事不能来，所以我们邀请了'+wcnames[-1].title())
print(wcnames[0].title(),wcnames[1].title(),wcnames[2].title(),wcnames[3].title()+juzi)
#3-6 又来
print(wcnames[0].title(),wcnames[1].title(),wcnames[2].title(),wcnames[3].title()+'我找到了一个更大的桌子，我还要邀请几个人！')
wcnames.insert(0,'gongshan')
wcnames.insert(2,'wanghua')
wcnames.append('lili')
print(wcnames[0].title(),wcnames[1].title(),wcnames[2].title(),wcnames[3].title(),wcnames[4].title(),wcnames[5].title()+juzi)
#3-7 桌子小了
print('因为刚买的桌子小了，只能邀请两位了')
print(wcnames.pop(0))
