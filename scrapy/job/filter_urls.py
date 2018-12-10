# -*- coding: utf-8 -*-
import re

f = open('urls_6711', 'rb')
s = open('urls_6711_filtered', 'wb')


patterns = [

    # 论坛 (论坛应该没有 参与改版)
    r'bbs\.6711\.com\/thread-\d+-\d+-\d+.html',  # bbs 帖子评论 分页
    r'bbs\.6711\.com\/viewthread\.php\?.+',  # 帖子
    r'bbs\.6711\.com\/viewthread\.php\?extra=',  # 帖子
    r'bbs\.6711\.com\/viewthread\.php\?authorid=\d+',  # 帖子
    r'bbs\.6711\.com\/viewthread\.php\?tid=\d+',  # 论坛帖子
    r'bbs\.6711\.com\/viewthread\.php\?action=printable&tid=\d+',  # 论坛帖子 打印版
    r'bbs\.6711\.com\/redirect.php\?goto=lastpost&tid=\d+',
    r'bbs\.6711\.com\/misc\.php\?action',  # 引导?
    r'bbs\.6711\.com\/post\.php\?action=reply',  # 回复话题
    r'bbs\.6711\.com\/post\.php\?action=newthread&fid=\d+',  # 添加话题
    r'bbs\.6711\.com\/index.html\?.+',
    r'bbs\.6711\.com\/forum-\d+-\d+.html',  # 游戏 论坛 翻页
    r'bbs\.6711\.com\/forumdisplay\.php\?fid=',  # 游戏 论坛 翻页 的动态链接, 改版后被 伪静态取代了
    r'bbs\.6711\.com\/my\.php\?buddysubmit=yes&item=buddylist&newbuddyid=\d+',
    r'bbs\.6711\.com\/space\.php\?.+',  # 个人空间
    r'bbs\.6711\.com\/pm\.php\?action=new&uid=\d+',  # 发送信息
    r'bbs\.6711\.com\/faq.php\?action=grouppermission',
    r'bbs\.6711\.com\/faq.php\?action=faq',
    r'bbs\.6711\.com\/faq.php\?action=credits',
    r'bbs\.6711\.com\/attachment\.php\?aid=',  # 附件, 图片居多
    r'bbs\.6711\.com\/admincp\.php\?action=settings',  # 管理员后台
    r'bbs\.6711\.com\/redirect\.php\?goto=',
    # ================== 改版  后 ==========================
    #  改版后的新闻 url, 所有游戏站群的文章页面都被分配到这边指使用 url 管理
    r'www\.6711\.com\/ziliao',
    r'www\.6711\.com\/servers_list_\w+.html',  # 游戏服务器列表
    r'www\.6711\.com\/huodong\/new_server\/\w+.php\?.+',
    r'www\.6711\.com\/news',
    r'www\.6711\.com\/open_server',
    r'www\.6711\.com\/yxgl',
    r'www\.6711\.com\/gamedata',  # 游戏的数据
    r'www\.6711\.com\/hdzx',  # 活动咨询
    r'www\.6711\.com\/wenxuan',  # 玩家文选
    r'www\.6711\.com\/gonglue',  # 攻略
    r'www\.6711\.com\/yxjt',  # 游戏截图
    r'www\.6711\.com\/yxzl',  # 游戏资料
    r'www\.6711\.com\/youxigonglue',  # 攻略
    r'www\.6711\.com\/youxiziliao',  # 攻略
    r'www\.6711\.com\/67phone\/',
    # ================== 改版  前 ==========================
    #  改版前的新闻 url, 游戏站群的文章归属于某个特定的目录
    r'www\.6711\.com\/\w+\/news',
    r'www\.6711\.com\/\w+\/open_server',
    r'www\.6711\.com\/\w+\/yxgl',
    r'www\.6711\.com\/\w+\/gamedata',  # 游戏的数据
    r'www\.6711\.com\/\w+\/hdzx',  # 活动咨询
    r'www\.6711\.com\/\w+\/wenxuan',  # 玩家文选
    r'www\.6711\.com\/\w+\/gonglue',  # 攻略
    r'www\.6711\.com\/\w+\/huodong',  # 活动
    r'www\.6711\.com\/\w+\/yxjt',  # 游戏截图
    r'www\.6711\.com\/\w+\/yxzl',  # 游戏资料
    r'www\.6711\.com\/\w+\/youxigonglue',  # 攻略
    r'www\.6711\.com\/\w+\/youxiziliao',  # 攻略
    r'www\.6711\.com\/\w+\/jietu',  # 攻略
    r'www\.6711\.com\/\w+\/zonghe',  # 攻略
    r'www\.6711\.com\/getcard_content\.html\?game=\w+',  # 礼品卡, 跳转 gift.6711
    r'www\.6711\.com\/6711_logout\.php\?local=',  # 退出登录, 跳转 my.6711.com
    r'www\.6711\.com\/game_login.html\?game=\w+&server=S\d+',  # 进游戏 跳转 game.67

    # 改版后的游戏登录链接 [游戏服务器] [游戏名] [fid?]
    r's\d+\.\w+\.6711\.com\/\?fid=',
    # 改版后的游戏支付链接 [游戏id] [游戏服务器id]
    r'pay\.6711\.com\/index\.php\?.+',
    r'pay\.6711\.com\/vpaymap\.html',  # 电信手机充值
    r'www\.6711\.com\/users',  # 改版前用户链接
    r'my\.6711\.com\/',  # 改版后用户链接
    r'gift\.6711\.com\/\?a=giftDetail&c=index&game_id=\d+&gift_id=\d+',
    r'game\.6711\.com\/\?c=play&game_id',

    # ================== 其它站点 ==========================
    # 百度授权接口
    r'openapi\.baidu\.com\/oauth',
    # qq 聊天
    r'wpa\.qq\.com\/msgrd\?Menu=yes',
]

for k in range(len(patterns)):
    patterns[k] = re.compile(patterns[k])

counter = 0
while True:
    l = f.readline()
    flag = False
    if not l:
        break
    for v in patterns:
        if v.search(l) is not None:
            flag = True
            break
    if flag:
        continue
    counter += 1
    s.write(l)

print(counter)

f.close()
s.close()

#
