import requests
import os
import json

session = requests.session()

pushplus_token = os.environ["PUSH_PLUS_TOKEN"]
#pushplus_token = ""
#是否打开推送开关
ispush = True

username = os.environ["11name"]
password = os.environ["11pwd"]
all_dict = {}
st = ""
tgw_l7_route = ""
cookie = ""
msg = ""

def login(user,pwd):
    global st,all_dict
    login_url = "https://olpassport.5211game.com/Login/Login"
    login_head = {
        "host": "olpassport.5211game.com",
        "content-length": "69",
        "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        "accept": "application/json, text/javascript, */*; q=0.01",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": '"Windows"',
        "origin": "https://olpassport.5211game.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://olpassport.5211game.com/Login?siteid=50008&returnUrl=https%3A//actnp.5211game.com/%23/&srvid=7",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    }

    login_data = {
        "user": user,
        "password": pwd,
        "code": "",
        "srvid": "7",
        "alive": "true"
    }
    login_response = session.post(url=login_url,headers=login_head,data=login_data)
    if login_response.status_code == 200 and login_response.json()['code'] == 1:
        st = login_response.json()['data']['st']
        all_dict["userName"] = login_response.json()['data']['userName']
        return True
    else:
        return False


def getuserinfo():
    global tgw_l7_route
    getuserinfo_url = f"https://actnp.5211game.com/newplayground/Home/GetUserInfo?st={st}"
    getuserinfo_head = {
        "host": "actnp.5211game.com",
        "sec-ch-ua": '";Not A Brand";v="99", "Chromium";v="94"',
        "accept": "application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://actnp.5211game.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cookie": "loginInfo=" + st
    }

    getuserinfo_response = session.get(url=getuserinfo_url,headers=getuserinfo_head)
    if getuserinfo_response.status_code == 200 and "操作成功" in getuserinfo_response.text:
        tgw_l7_route = requests.utils.dict_from_cookiejar(getuserinfo_response.cookies)['tgw_l7_route']
        return True
    else:
        return False

def getcharglist():
    global all_dict
    getcharglist_url = f"https://actnp.5211game.com/newplayground/RS/GetChargeList?st={st}&page_index=1&page_size=99999&ctype=1"
    getcharglist_head = {
        "host": "actnp.5211game.com",
        "sec-ch-ua": '";Not A Brand";v="99", "Chromium";v="94"',
        "accept": "application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://actnp.5211game.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cookie": "tgw_l7_route=" + tgw_l7_route + ";loginInfo=" + st
    }
    getcharglist_response = session.get(url=getcharglist_url,headers=getcharglist_head)
    if getcharglist_response.status_code == 200 and "操作成功" in getcharglist_response.text:
        all_dict["honor_essence"] = str(getcharglist_response.json()['data']['honor_essence'])
        all_dict["limit_skin_chip"] = str(getcharglist_response.json()['data']['limit_skin_chip'])
        all_dict["box_chip"] = str(getcharglist_response.json()['data']['box_chip'])
        all_dict["skin_essence"] = str(getcharglist_response.json()['data']['skin_essence'])
        return True
    else:
        return False

def getfreebox():
    global all_dict
    getfreebox_url = f"https://actnp.5211game.com/newplayground/RS/RcvDayOne?st={st}"
    getfreebox_head = {
        "host": "actnp.5211game.com",
        "sec-ch-ua": '";Not A Brand";v="99", "Chromium";v="94"',
        "accept": "application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://actnp.5211game.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cookie": "loginInfo=" + st
    }
    getfreebox_response = session.get(url=getfreebox_url,headers=getfreebox_head)
    if getfreebox_response.status_code == 200:
        all_dict["box_msg"] = str(getfreebox_response.json()['msg'])
        return True
    else:
        return False

def gettaskdata(tp):
    global cookie
    gettaskdata_url = "https://actdota.5211game.com/lbps2023/JP/GetTaskData"
    gettaskdata_head = {
        "host": "actdota.5211game.com",
        "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        "accept": "*/*",
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": '"Windows"',
        "origin": "https://actdota.5211game.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://actdota.5211game.com/lbps2023",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cookie": cookie
    }
    gettaskdata_data = {
        "tp": tp
    }
    gettaskdata_response = session.post(url=gettaskdata_url,headers=gettaskdata_head,data=gettaskdata_data)
    for dic in gettaskdata_response.json()['data']['lst_tasks']:
        if dic['flag'] == 0:
            if dealtask(dic['tid']):
                msgbox(f"{dic['tname']}奖励领取成功!")
            else:
                msgbox(f"{dic['tname']}奖励领取失败!")
        elif dic['flag'] == 1:
            msgbox(f"{dic['tname']}奖励已经领取!")


def dealtask(tid):
    dealtask_url = "https://actdota.5211game.com/lbps2023/JP/RcvTask"
    dealtask_head = {
        "host": "actdota.5211game.com",
        "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        "accept": "*/*",
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": '"Windows"',
        "origin": "https://actdota.5211game.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://actdota.5211game.com/lbps2023",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cookie": cookie
    }
    dealtask_data ={
        "tid": tid
    }
    dealtask_response = session.post(url=dealtask_url,headers=dealtask_head,data=dealtask_data)
    if dealtask_response.status_code == 200 and "操作成功" in dealtask_response.json()['msg']:
        return True
    else:
        return False

def getcookie():
    global cookie
    cookie =""
    getcookie_url = f"https://actdota.5211game.com/lbps2023/Passport?returnurl=http://actdota.5211game.com/lbps2023&st={st}"
    getcookie_head = {
        "host": "actdota.5211game.com",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cookie": f"tgw_l7_route={tgw_l7_route}"
    }
    getcookie_response = session.get(url=getcookie_url,headers=getcookie_head,allow_redirects=False)
    if getcookie_response.status_code == 302:
        cookies=dict(requests.utils.dict_from_cookiejar(getcookie_response.cookies))
        for key in cookies.keys():
            cookie = cookie + key + "=" + cookies[key] + ";"
        return True
    else:
        return False

def msgbox(str):
    global msg
    if ispush:
        msg = msg + "\n" + str
    print(str)

if __name__ == '__main__':
  if login(username,password):

      print("【11Game用户】" + all_dict["userName"] + " 登陆成功！")
      if getuserinfo():
          msgbox("【11Game用户】" + all_dict["userName"] + " 信息获取成功！")
          if getcharglist():
              msgbox("【荣耀精粹】" + all_dict["honor_essence"])
              msgbox("【限定碎片】" + all_dict["limit_skin_chip"])
              msgbox("【宝箱碎片】" + all_dict["box_chip"])
              msgbox("【皮肤碎片】" + all_dict["skin_essence"])
          if getfreebox():
              msgbox("【开宝箱结果】" + all_dict["box_msg"])
          if getcookie():
              print("【任务获取及奖励领取】")
              for tp in range(1,5):
                  gettaskdata(tp)
          msgbox("【任务执行完毕】")
          if ispush:
              requests.get('http://www.pushplus.plus/send?token=' + pushplus_token + '&title=11Game开宝箱&content=' + msg)
              print("【Pushplus】消息推送成功！")
          else:
              print("【Pushplus】消息推送开关未打开！")
