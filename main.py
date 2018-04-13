import requests
import json
from config import Config
from MsgHandler import Notify

# 主要程序進入入口
def main():
    config = Config()
    s = requests.session()
    # 取csrf token
    getCsrf = s.get("https://www.dcard.tw/_api/_ping")
    # 登入
    account,password = config.GetDcardAccount()
    payload = {"email": account, "password": password}
    getSession = s.post('https://www.dcard.tw/_api/sessions', json=payload,headers= {'x-csrf-token': getCsrf.headers["x-csrf-token"]})
    if getSession.text:
        loginResult = json.loads(getSession.text)
        if loginResult["error_description"]=="Password mismatch":
            raise  Exception("D卡帳號密碼錯誤")

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
        # print(Name,content,msgId)
        # 取得通知的設定
        NotifyWays = config.GetNotifyWay()
        for notifyType,settings in NotifyWays.items():
            # 如果此通知為啟用
            if settings["IsEnable"]:
                Notify(Name,content,msgId,notifyType,settings)




if __name__ == '__main__':
    main()