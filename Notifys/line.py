import requests

# 記得實作send()方法
class line():
    def __init__(self,token, msg):
        self.token = token
        self.msg = msg

    def send(self):
        url = "https://notify-api.line.me/api/notify"
        headers = {
            "Authorization": "Bearer " + self.token
        }

        payload = {'message': self.msg}
        r = requests.post(url, headers=headers, params=payload)
        return r.status_code

if __name__ == '__main__':
    # 取得token的方法請參考此篇參考這篇設置http://studyhost.blogspot.tw/2016/12/linebot6-botline-notify.html
    token = "zxSeJ7zfqOcttg04N7np5GUDiebbqZvXJ6WDyhO2F6n"
    msg = "Hello Python"

    line(token, msg).send()