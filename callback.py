import falcon
import json
from linebot import LineBotApi, WebhoookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMssage

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN = '7pp1e5yQqTj7AEWAJIzk/B9pa1WDqJJbUCbwbCH4cdSI/A1RDST5RfAxw9TfZD9OPYo4vNTkfWZyELrXD9TRMpMqN60pohkbwpQM0e55i33Ycd3EGcxVGSKA+YhrV7OcMfoeHHhAawSDjAUnkhTA0QdB04t89/1O/w1cDnyilFU='
CHANNEL_SECRET = '973f214ae9a2cc10b4497e80201973b9'
line_bot_api = LineBotApi(ACCES_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

class Resource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "Hello, World"

    def on_post(self, req, resp):
        signature = req.headers['X-LINE-Signature']
        body = req.stream.read()
        body = json.loads(body.decode('utf-8'))
        replyToken = body['events'][0]['replayToken']
        
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

@handler.add(MessageEvent, mesage=TextMessage)
def handle_mesage(event):
    line_bot_api.reply_message(event['events']['replyToken'], TextSendMessage(text=event['events'][0]['message']['text'])
                               
app = falcon.API()

app.add_route('/callback', Resource())

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
    
