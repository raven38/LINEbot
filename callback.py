import falcon
import json
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

ACCESS_TOKEN = 'access_token'
CHANNEL_SECRET = 'channel_secret'
line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

class Resource(object):
    def on_post(self, req, resp):
        print(req.headers)
        signature = req.headers['X-LINE-SIGNATURE']
        body = req.stream.read()
        body = body.decode('utf-8')
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)


@handler.add(MessageEvent, message=TextMessage)
def handle_mesage(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))
                               
app = falcon.API()
app.add_route('/callback', Resource())
    
