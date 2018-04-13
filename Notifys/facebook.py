from fbchat import Client
from fbchat.models import *
# p.s. 此用法facebook不會出現通知 因此放棄此方法
# 記得實作send()方法
class fb():
    def send(self):
        client = Client('帳號', '密碼')
        client.send(Message(text='Hi me!'), thread_id=client.uid, thread_type=ThreadType.USER)
        client.logout()

if __name__ == '__main__':
    fb()