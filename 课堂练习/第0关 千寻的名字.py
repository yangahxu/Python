# #欢迎
import time
print('你来和我做朋友了吗？我好高兴啊！让我来介绍一下自己')
time.sleep(2)
print('有人说：我是迈入人工智能时代的第一道门槛。')
time.sleep(2)
print('这没错，确实有很多人工智能算法都是通过我来实现的')
time.sleep(2)
print('还有人说，我是编程初学者入门的最好选择')
time.sleep(1)
print('这也对，因为我还被称为"胶水语言"，是最简洁的编程语言了')
time.sleep(2)
print('但是，对你而言，我究竟应该是什么呢？')
time.sleep(1)
print('其实，我是你实现目的的一个工具，只要你有需求，我就能帮上忙')
time.sleep(2)
print('''我会好好地帮助你，带你紧跟人工智能时代;
我会解放你的双手，帮你提高工作效率；''')

#图片识别
import requests
from aip import AipOcr

image = requests.get('https://static.pandateacher.com/7b5d6d8d9dea5691705d04fef2306b52.png').content

APP_ID = '16149264'
API_KEY = 'yxYg9r4OuAs4fYvfcl8tqCYd'
SECRET_KEY = 'yWg3KMds2muFsWs7MBSSFcgMQl8Wng4s'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
res = client.basicGeneral(image)
if 'words_result' in res.keys():
    for item in res['words_result']:
        print(item['words'])
else:
    print(res)

#猜年龄
import time,random
print('''============================
          埋める年齢
======================''')
time.sleep(2)
print('你好呀ヽ✿゜▽゜)ノ我叫小埋~想和我玩吗？先猜对我的年龄吧~~')
time.sleep(2)
user_guess=int(input('我的年龄在1-10岁之间，请输入你猜的答案吧(◆◡◆)（必须是整数1-10哦）'))
print('哦~~你猜我'+str(user_guess)+'岁呀，来看看你猜的对不对……')
time.sleep(2)
age=random.randint(1,10)
if user_guess==age:
    print('嘻嘻！猜对啦！我们做好朋友吧（￣︶￣）↗再见啦！')
elif user_guess<age:
    print('猜错啦！我才没有那么小呢(＞﹏＜)不和你玩了！')
else:
    print('猜错啊！我才没有那么老呢（；´д｀）ゞ不和你玩了！')

#人工智能小程序
import requests, json, time, random

word = input('''你好，我是你的私人助理吴小枫。你可以在下方任意输入一个名词，然后敲击“Enter”键，我将会帮你自动联想它有什么相关的词汇！
注：如果你要删除自己输入的内容，要按两次删除，才可以删掉一个汉字奥！（因为在计算机世界里，中文是占两个字符的！）
下面请输入（示例：牛肉、水果、飞机、手机……），然后敲“Enter”：
>''')
word=word+'有哪些相关词汇？'
feature_text = '''
我们可以先聊点别的，我还有什么可以帮助你的吗？
输入你的问题，然后敲Enter键！
>'''

url1 = 'http://ictclas.nlpir.org/nlpir/index/getAllContentNew.do'
data1 = {'type': 'all', 'content': word}
try:
    r1 = requests.post(url1, data1, timeout=3)
    dividewords = json.loads(r1.text)['dividewords']
    dividewords = dividewords.split(' ')
    newwords = []
    cixing = []
    for x in dividewords:
        if x == dividewords[-1]:
            continue
        else:
            singleword = x.split('/')
            newwords.append(singleword[0])
            cixing.append(singleword[1])
    newlist = '/'.join(newwords)
    dict = {'n': '名词', 'nr': '人名', 'nr1': '汉语姓氏', 'nr2': '汉语名字', 'nrj': '日语人名', 'nrf': '音译人名', 'ns': '地名',
            'nsf': '音译地名', 'nt': '机构团体名', 'nz': '其它专名', 'nl': '名词性惯用语', 'ng': '名词性语素',
            't': '时间词', 'tg': '时间词性语素', 's': '处所词', 'f': '方位词',
            'v': '动词', 'vd': '副动词', 'vn': '名动词', 'vshi': '动词“是”', 'vyou': '动词“有”', 'vf': '趋向动词', 'vx': '形式动词',
            'vi': '不及物动词（内动词）', 'vl': '动词性惯用语', 'vg': '动词性语素',
            'a': '形容词', 'ad': '副形词', 'an': '名形词', 'ag': '形容词性语素', 'al': '形容词性惯用语', 'b': '区别词', '': '',
            'bl': '区别词性惯用语',
            'z': '状态词',
            'r': '代词', 'rr': '人称代词', 'rz': '指示代词', 'rzt': '时间指示代词', 'rzs': '处所指示代词', 'rzv': '谓词性指示代词', 'ry': '疑问代词',
            'ryt': '时间疑问代词', 'rys': '处所疑问代词', 'ryv': '谓词性疑问代词', 'rg': '代词性语素',
            'm': '数词', 'mq': '数量词', 'q': '量词', 'd': '副词', 'p': '介词', 'pba': '介词“把”', 'pbei': '介词“被”', 'c': '连词',
            'cc': '并列连词',
            'u': '助词', 'uzhe': '着', 'ule': '了，喽', 'uguo': '过', 'ude1': '的', 'ude2': '地', 'ude3': '得', 'usuo': '所',
            'udeng': '等，等等，云云', 'uyy': '一样，一般，似的，般', 'udh': '的话', 'uls': '来讲，来说，而言，说来', 'uzhi': '之', 'ulian': '连',
            'e': '叹词', 'y': '语气词', 'o': '拟声词', 'h': '前缀', 'k': '后缀', 'x': '字符串', 'xe': 'Email字符串', 'xs': '微博会话分隔符',
            'xm': '表情符合', 'xu': '网址URL',
            'w': '标点符号', 'wkz': '左括号', 'wky': '右括号', 'wyz': '左引号', 'wj': '句号', 'ww': '问号', 'wt': '叹号', 'wd': '逗号',
            'wf': '分号', 'wn': '顿号', 'wm': '冒号', 'ws': '省略号', 'wp': '破折号', 'wb': '百分号千分号', 'wh': '单位符号'
            }
    time.sleep(1)
    print('\n首先，我帮你补全了问题，你问的是：'+word+'有哪些相关词汇，对吗？')
    print('\n接着，我先把你的话做了分词：' + newlist + '。')
    cixinglist = ''
    for y in cixing:
        cixinglist = cixinglist + dict[y] + '/'
    time.sleep(2)
    print('它们的词性分别是：' + cixinglist + '。')
    time.sleep(2)
    print('其中，我判断' + newwords[0] + '是一个' + dict[cixing[0]] + '，你问我的是它的相关词汇有哪些对吗？')
    url = 'http://ictclas.nlpir.org/nlpir/index6/getWord2Vec.do'
    data = {'content': newwords[0]}
    r = requests.post(url, data)
    other = json.loads(r.text)
    time.sleep(1)
    print ('\n我想了想和“' + newwords[0] + '”相关的词汇，至少还有：\n')
    time.sleep(1)
    f = 0
    for i in other['w2vlist']:
        f = f + 1
        word2 = i.split(',')
        print ('(' + str(f) + ')' + word2[0] + '，其相关度为' + word2[1])
        time.sleep(1)
    feature_text = '''
现在，你已经解锁我的所有功能，可以自由聊天啦！我还有什么可以帮助你的吗？
回复内容，然后敲Enter键！
>'''
except requests.exceptions.ConnectTimeout:
    print('额,抱歉,网络连接失败了,词汇拆解功能暂时无法使用...')
except requests.exceptions.Timeout:
    print('额,抱歉,网络连接超时了,词汇拆解功能暂时无法使用...')

user1 = input(feature_text)
time.sleep(1)
userid = str(random.randint(1, 1000000000000000000000))
apikey = 'd81c0b99c260440980a140440be200ec'
#超过1w有风险，19-01-19
tulingdata1 = json.dumps({    "perception": {
        "inputText": {
            "text": user1
        },

    },
    "userInfo": {
        "apiKey": apikey,
        "userId": userid
    }
})
robot1 = requests.post('http://openapi.tuling123.com/openapi/api/v2', tulingdata1)
jsrobot1 = json.loads(robot1.text)['results'][0]['values']['text']
print(jsrobot1)
time.sleep(2)
user2 = input('''
再和你聊最后一句我就要下线了奥，你还有什么要求吗？
回复内容，然后敲Enter键！
>''')
tulingdata1 = json.dumps({
    "perception": {
        "inputText": {
            "text": user2
        },

    },
    "userInfo": {
        "apiKey": apikey,
        "userId": userid
    }
})
robot1 = requests.post('http://openapi.tuling123.com/openapi/api/v2', tulingdata1)
jsrobot1 = json.loads(robot1.text)['results'][0]['values']['text']
time.sleep(1)
print(jsrobot1)
time.sleep(1)
print('\n我走啦，下次见！')
#第一串代码
import time
print ('在'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'，我写了人生中第一行Python代码\n它的内容虽然简单，不过是平凡的一句print(520)\n但我知道：我的编程之路，将从最简单的520开始\n在我点击运行的同时，一切在这一刻开始变得不同\n以下，是这行代码的运算结果：' )
print (520)