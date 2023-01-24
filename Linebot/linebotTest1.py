from flask import Flask
app = Flask(__name__)

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent,TextMessage, TextSendMessage
from googletrans import Translator

line_bot_api = LineBotApi('oCxMpz4SLBRSEE60cURkiq/7UUs2vVMnWfdqmP3+MbfiBqMmADDRr6NkaLkooKnOi6NlRvmsvvswEl3k5BoBwUuBfGGx6BskLKyNll/fotFIziSQLM56FPUDv4sYPgF42yrunqbUQgjW3hyH0wwvYwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('64d5776ef72131c31b0d984f20550a82')
translator = Translator()


@app.route("/callback", methods = ['POST'])
def callback():
    signature = request.headers['X-Line_Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    detection = translator.detect(event.message.text)
    if detection.lang =='en':
        translation_text = translator.translate(event.message.text, dest='zh-tw')
    else: 
        translation_text = translator.translate(event.message.text, dest='en')
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=translation_text.text))

if __name__ == '__main__':
    app.run()
