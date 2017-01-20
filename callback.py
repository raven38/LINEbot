import falcon
import json
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

ACCESS_TOKEN = '7pp1e5yQqTj7AEWAJIzk/B9pa1WDqJJbUCbwbCH4cdSI/A1RDST5RfAxw9TfZD9OPYo4vNTkfWZyELrXD9TRMpMqN60pohkbwpQM0e55i33Ycd3EGcxVGSKA+YhrV7OcMfoeHHhAawSDjAUnkhTA0QdB04t89/1O/w1cDnyilFU='
CHANNEL_SECRET = '973f214ae9a2cc10b4497e80201973b9'
line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

class Resource(object):
    def on_post(self, req, resp):
#        print(req.headers)
        signature = req.headers['X-LINE-SIGNATURE']
        body = req.stream.read()
        body = body.decode('utf-8')
        try:
            handler.handle(body, signature)
        except InvalidSignatureError as e:
            print(e)
#            abort(400)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
#    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))
    print(type(event.message.text))
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text='こんにちは'))
                               
app = falcon.API()
app.add_route('/callback', Resource())
    
