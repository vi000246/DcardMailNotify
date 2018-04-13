import requests
import json


def main():
    s = requests.session()
    # 取csrf tokey
    getCsrf = s.get("https://www.dcard.tw/_api/_ping")
    # 登入
    payload = {"email": "vi000246@gmail.com", "password": "uish2013"}
    getSession = s.post('https://www.dcard.tw/_api/sessions', json=payload,headers= {'x-csrf-token': getCsrf.headers["x-csrf-token"]})
    # 取得信件夾各朋友最後發送的訊息
    r = s.get("https://www.dcard.tw/_api/me/messages",headers = {'x-csrf-token': getSession.headers["x-csrf-token"]})
    msgs = json.loads(r.text)
    # 如果unread=1代表未讀  currentMember=True代表訊息是我發出 可用來判斷是否回覆
    unreadMsg = [x for x in msgs if x['unread'] == 0]
    # print(unreadMsg)
    for msg in unreadMsg:
        Name = msg["speaker"]["name"] # 發訊息的人
        content = msg["content"] # 內容
        msgId = msg["id"] # 訊息編號
        print(Name,content,msgId)




if __name__ == '__main__':
    main()