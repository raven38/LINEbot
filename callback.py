import falcon
import json

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'


class Resource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200 
        resp.body = ("Hello, World")
        
    def on_post(self, req, resp):
        body = req.stream.read()        
        data = json.loads(body.decode('utf-8'))
#        replyToken = data['replayToken']

        
        resp.status = falcon.HTTP_200 # This is the default status
        resp.set_headers([("Content-Type","application/json"),("Authorization","Bearer 7pp1e5yQqTj7AEWAJIzk/B9pa1WDqJJbUCbwbCH4cdSI/A1RDST5RfAxw9TfZD9OPYo4vNTkfWZyELrXD9TRMpMqN60pohkbwpQM0e55i33Ycd3EGcxVGSKA+YhrV7OcMfoeHHhAawSDjAUnkhTA0QdB04t89/1O/w1cDnyilFU=")])

        msg = {
 #           "replyToken":replyToken,
            "messages":{
                "type":"text",
                "text":"Hello, World\n"
                }
        }
        resp.body = json.dumps(msg)
#        resp.body = body.decode('utf-8')

app = falcon.API()

app.add_route('/callback', Resource())

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
    
