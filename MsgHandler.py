# 處理通知的方式
class Notify:
    # speaker:訊息發送人 content:內容 notifyType:訊息類形
    def __init__(self, speaker, content, notifyType):
        self.speaker = speaker
        self.content = content
        self.notifyType = notifyType
