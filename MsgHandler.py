from Notifys import facebook,line
# 處理通知的方式
class Notify:
    # speaker:訊息發送人 content:內容 msgId:訊息的編號 notifyType:要用的通知類形 notifySetting:通知的設定
    def __init__(self, speaker, content,msgId, notifyType,notifySetting):
        self.speaker = speaker
        self.content = content
        self.notifyType = notifyType
        self.msgId = msgId
        self.notifySetting = notifySetting
        notify = self.getNotifyWay()
        notify.send()

    # 依據notifyType 取得對應class
    def getNotifyWay(self):
        if self.notifyType == "facebook":

            return facebook.fb()
        elif self.notifyType == "line":

            return line.line("zxSeJ7zfqOcttg04N7np5GUDiebbqZvXJ6WDyhO2F6n","測試中文")
        else:
            raise Exception("查無此通知方式")

if __name__ == '__main__':
    Notify("test","msg","id","line",{"test":"123"})


