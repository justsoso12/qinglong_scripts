"""
cron: 45 1 * * *
new Env('11Game领取奖励');
"""
import requests
import os
import json

session = requests.session()

pushplus_token = os.environ["PUSH_PLUS_TOKEN"]
#pushplus_token = ""
#是否打开推送开关
ispush = True

username = os.environ["name_11game"]
password = os.environ["pwd_11game"]
all_dict = {}
indexed = []
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

def gettaskinfos():
    gettaskinfos_url = f"https://actnp.5211game.com/newplayground/BZ/GetTaskInfos?st={st}"
    gettaskinfos_head = {
        "Host": "actnp.5211game.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": '"Windows"',
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://actnp.5211game.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cookie": "tgw_l7_route=" + tgw_l7_route + ";loginInfo=" + st
    }
    gettaskinfos_response = session.get(url=gettaskinfos_url,headers=gettaskinfos_head)
    if gettaskinfos_response.status_code == 200 and "操作成功" in gettaskinfos_response.text:
        msgbox("【宝藏每日任务】领取情况：")
        for tasks in gettaskinfos_response.json()['data']['lstDayTasks']:
            if tasks['flag'] == 0:
                if dealtaskinfos(tasks['task_id']):
                    msgbox(f"{tasks['task_name']} 任务进度（{tasks['V']}/{tasks['C']}）领取成功！")
                else:
                    msgbox(f"{tasks['task_name']} 任务进度（{tasks['V']}/{tasks['C']}）领取失败！")
            elif tasks['flag'] == 1:
                msgbox(f"{tasks['task_name']} 任务进度（{tasks['V']}/{tasks['C']}）已经领取！")
            else:
                msgbox(f"{tasks['task_name']} 任务进度（{tasks['V']}/{tasks['C']}）未达标！")
        msgbox("【宝藏每周任务】领取情况：")
        for tasks in gettaskinfos_response.json()['data']['lstWeekTasks']:
            if tasks['flag'] == 0:
                if dealtaskinfos(tasks['task_id']):
                    msgbox(f"{tasks['task_name']} 任务进度（{tasks['V']}/{tasks['C']}）领取成功！")
                else:
                    msgbox(f"{tasks['task_name']} 任务进度（{tasks['V']}/{tasks['C']}）领取失败！")
            elif tasks['flag'] == 1:
                msgbox(f"{tasks['task_name']} 任务进度（{tasks['V']}/{tasks['C']}）已经领取！")
            else:
                msgbox(f"{tasks['task_name']} 任务进度（{tasks['V']}/{tasks['C']} ）未达标！")
        return True
    else:
        return False

def dealtaskinfos(tid):
    dealtaskinfos_url = f"https://actnp.5211game.com/newplayground/BZ/RcvTaskGift?st={st}&tid={tid}"
    dealtaskinfos_head = {
        "Host": "actnp.5211game.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": '"Windows"',
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://actnp.5211game.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cookie": "tgw_l7_route=" + tgw_l7_route + ";loginInfo=" + st
    }
    dealtaskinfos_response = session.get(url=dealtaskinfos_url,headers=dealtaskinfos_head)
    if dealtaskinfos_response.status_code == 200 and "操作成功" in dealtaskinfos_response.text:
        return True
    else:
        return False

def getgridtimes():
    global indexed
    getgridtimes_url = f"https://actnp.5211game.com/newplayground/BZ/GetGridTimes?st={st}"
    getgridtimes_head = {
        "Host": "actnp.5211game.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": '"Windows"',
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://actnp.5211game.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cookie": "tgw_l7_route=" + tgw_l7_route + ";loginInfo=" + st
    }
    getgridtimes_response = session.get(url=getgridtimes_url,headers=getgridtimes_head)
    if getgridtimes_response.status_code == 200 and "操作成功" in getgridtimes_response.text:
        times = getgridtimes_response.json()['data']
        msgbox(f"【宝藏可开箱次数】 {times}次")
        if times >0:
            for a in range(0,times):
                for b in range(1,51):
                    if b not in indexed:
                        if openbox(b):
                            indexed.append(b)
                        break

def openbox(index):
    openbox_url = f"https://actnp.5211game.com/newplayground/BZ/RcvGridGift?st={st}&index={index}"
    openbox_head = {
        "Host": "actnp.5211game.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": '"Windows"',
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://actnp.5211game.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cookie": "tgw_l7_route=" + tgw_l7_route + ";loginInfo=" + st
    }
    openbox_response = session.get(url=openbox_url,headers=openbox_head)
    if openbox_response.status_code == 200 and "操作成功" in openbox_response.text:
        msgbox(f"【宝藏开宝箱】获取到【{openbox_response.json()['data']['show_name']}】")
        return True
    else:
        return False



def boxdetail():
    global indexed
    boxdetail_url = f"https://actnp.5211game.com/newplayground/BZ/GetUserGridDetail?st={st}"
    boxdetail_head = {
        "Host": "actnp.5211game.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": '"Windows"',
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://actnp.5211game.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cookie": "tgw_l7_route=" + tgw_l7_route + ";loginInfo=" + st
    }
    boxdetial_response = session.get(url=boxdetail_url,headers=boxdetail_head)
    if boxdetial_response.status_code == 200 and "操作成功" in boxdetial_response.text:
        msgbox("【宝藏宝箱】开启情况：")
        for dic in boxdetial_response.json()['data']:
            if dic['is_opened']:
                indexed.append(dic['index'])
                msgbox(f"【宝藏宝箱】index:{dic['index']} {dic['show_name']} 已开启！")
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

def getdata():
    global cookie
    getdata_url = "https://actdota.5211game.com/LBPS202351/JP/GetData"
    getdata_head = {
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
        "referer": "https://actdota.5211game.com/LBPS202351",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cookie": cookie
    }
    getdata_response = session.post(url=getdata_url,headers=getdata_head)
    if getdata_response.status_code == 200:
        print(getdata_response.text)

def gettaskdata(tp):
    global cookie
    gettaskdata_url = "https://actdota.5211game.com/LBPS202351/JP/GetTaskData"
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
        "referer": "https://actdota.5211game.com/LBPS202351",
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
    dealtask_url = "https://actdota.5211game.com/LBPS202351/JP/RcvTask"
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
        "referer": "https://actdota.5211game.com/LBPS202351",
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
    getcookie_url = f"https://actdota.5211game.com/LBPS202351/Passport?returnurl=http://actdota.5211game.com/LBPS202351&st={st}"
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
              msgbox("【碎片数量】统计：")
              msgbox("【荣耀精粹】" + all_dict["honor_essence"])
              # msgbox("【限定碎片】" + all_dict["limit_skin_chip"])
              msgbox("【宝箱碎片】" + all_dict["box_chip"])
              msgbox("【皮肤碎片】" + all_dict["skin_essence"])
          if gettaskinfos():
              print("【宝藏任务执行完毕】")
          if boxdetail():
              getgridtimes()
          if getfreebox():
              msgbox("【每日免费宝箱】" + all_dict["box_msg"])
          if getcookie():
              print("【夏季通行证任务】领取情况：")
              for tp in range(1,5):
                  gettaskdata(tp)
          msgbox("【任务执行完毕】")
          if ispush:
              requests.get('http://www.pushplus.plus/send?token=' + pushplus_token + '&title=11Game开宝箱&content=' + msg)
              print("【Pushplus】消息推送成功！")
          else:
              print("【Pushplus】消息推送开关未打开！")
