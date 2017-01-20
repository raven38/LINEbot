import falcon
import json
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

ACCESS_TOKEN = '************'
CHANNEL_SECRET = '************'
line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

class Resource(object):
    def on_post(self, req, resp):
        signature = req.headers['X-LINE-SIGNATURE']
        body = req.stream.read()
        body = body.decode('utf-8')
        try:
            # handlerは登録したhandleを自動的に割り当てる
            handler.handle(body, signature)
        except InvalidSignatureError as e:
            print(e)

# 実際のreplyの本体、TextSendMessageの引数textに送りたいstrを設定する
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))

    
app = falcon.API()
app.add_route('/callback', Resource())
    
