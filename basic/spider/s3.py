#! /usr/bin/python3
# 爬取有道翻译接口
def youdao(word):
    import hashlib
    import requests
    import time
    import random
    import re

    appVersion = '5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    # 浏览器调试后发现ts是时间戳
    ts = str(int(time.time() * 1000))
    # bv是请求头里面浏览器的信息经过MD5加密
    bv = hashlib.md5(appVersion.encode('utf-8')).hexdigest()
    # salt是时间戳后面随机加一位数字[0,9]
    salt = ts + str(random.randint(0, 9))
    sign_str = "fanyideskweb" + word + salt + "@6f#X3=cCuncYssPsuRUE"
    # sign是上面这个字符串MD5后的结果
    sign = hashlib.md5(sign_str.encode('utf-8')).hexdigest()
    # print(ts)
    # print(bv)
    # print(salt)

    # request请求地址
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    # 请求头
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "258",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=1011964969@10.169.0.83; JSESSIONID=aaa2xaVAnC78n4KVSHwUw; OUTFOX_SEARCH_USER_ID_NCOO=280669685.8154466; ___rl__test__cookies=1561601226382",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    # 请求数据，json字符串，其中salt，sign，ts,bv的值每次请求都会变
    data = {
        "i": word,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "ts": ts,
        "bv": bv,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION"
    }

    response = requests.post(url, data=data, headers=headers)
    ret = response.text
    # 正则匹配到需要的翻译结果
    retRegex = re.compile(r'"translateResult":(.*),"errorCode".*')
    translateResult = retRegex.search(ret).group(1)
    return translateResult


while True:
    word = input("请输入你需要翻译的词汇（回车退出）：")
    if word == '':
        break
    else:
        print(youdao(word))
