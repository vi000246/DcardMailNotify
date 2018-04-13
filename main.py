import requests
import json


def login():
    s = requests.session()
    # 取csrf tokey
    getCsrf = s.get("https://www.dcard.tw/_api/_ping")
    # 登入
    payload = {"email": "vi000246@gmail.com", "password": "uish2013"}
    getSession = s.post('https://www.dcard.tw/_api/sessions', json=payload,headers= {'x-csrf-token': getCsrf.headers["x-csrf-token"]})
    # 取得信件夾最後發送的訊息 依照各朋友分區
    r = s.get("https://www.dcard.tw/_api/me/messages",headers = {'x-csrf-token': getSession.headers["x-csrf-token"]})
    msg = json.loads(r.text)
    # 如果unread=1代表未讀  currentMember用來判斷是否已回覆
    output_dict = [x for x in msg if x['unread'] == 0]
    print(output_dict)



if __name__ == '__main__':
    login()