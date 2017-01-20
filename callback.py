import falcon
import json
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

ACCESS_TOKEN = 'zQSxDZOVNQ6P6xHaDmuM5WZqdoREQUNknDqBscHBFzNYLzk/qvPm2G0MniAA3FyLM3aLIbZB2Tn2jKHarFasmhFGICYVOVdhZPhNtq3mybPS3cTFXgP6hKGUgKx/pONldRPt7cCJQuJWPl6UsYKthQdB04t89/1O/w1cDnyilFU='
CHANNEL_SECRET = 'dd1e8da2217482d939cbda0fb4b52b50'
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
    
