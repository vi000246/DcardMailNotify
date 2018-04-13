import yaml
# 用來取得config檔
class Config:

    def __init__(self):
        # 讀取文件
        f = open('config.yaml' , encoding = 'utf8')
        # 導入
        self.config = yaml.load(f)

    # 取得D卡帳密 回傳tuple
    def GetDcardAccount(self):
        account = self.config["DcardLogin"]["Account"]
        password = self.config["DcardLogin"]["Password"]
        if account == None or password == None:
            raise Exception("請設置D卡的帳號密碼")
        return (account,password)

    # 取得通知設置
    def GetNotifyWay(self):
        NotifyWays = self.config["Notify"]
        print(NotifyWays)



if __name__ == '__main__':
    config = Config()
    print(config.GetDcardAccount())
    config.GetNotifyWay()

