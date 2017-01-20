from wsgiref import simple_server
import falcon
import json
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN = '7pp1e5yQqTj7AEWAJIzk/B9pa1WDqJJbUCbwbCH4cdSI/A1RDST5RfAxw9TfZD9OPYo4vNTkfWZyELrXD9TRMpMqN60pohkbwpQM0e55i33Ycd3EGcxVGSKA+YhrV7OcMfoeHHhAawSDjAUnkhTA0QdB04t89/1O/w1cDnyilFU='
CHANNEL_SECRET = '973f214ae9a2cc10b4497e80201973b9'
line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

class Resource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "Hello, World"

    def on_post(self, req, resp):
<<<<<<< HEAD
=======
        print(req.headers)
        signature = req.headers['X-LINE-SIGNATURE']
        body = req.stream.read()
        body = body.decode('utf-8')
#        body = json.loads(body.decode('utf-8'))
#        replyToken = body['events'][0]['replyToken']
>>>>>>> d97c76e9f363cd08394de3e00724abf7289949cf

        
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

@handler.add(MessageEvent, message=TextMessage)
def handle_mesage(event):
    print(type(event))
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))
                               
app = falcon.API()

app.add_route('/callback', Resource())

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
    
