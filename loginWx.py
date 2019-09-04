from wxpy import *
bot = Bot(cache_path=True)

girl_friend = bot.search('Candy')[0]
print(girl_friend)


# 接收从指定好友发来的消息，发送者即recv_msg.sender为指定好友girl_friend
@bot.register(chats=girl_friend)
def recv_send_msg(recv_msg):
    print('收到的消息：', recv_msg.text)  # recv_msg.text取得文本
    if recv_msg.sender == girl_friend:
        # 在文件传输助手里留一份，方便自己忙完了回头查看
        recv_msg.forward(bot.file_helper, prefix='老婆留言: ')
        return '老婆最美丽，我对老婆的爱如滔滔江水，连绵不绝'  # 给老婆回一份


embed()
