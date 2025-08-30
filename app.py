import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from dotenv import load_dotenv

load_dotenv(override=True)

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ["ACCESS_TOKEN"])
handler = WebhookHandler(os.environ["CHANNEL_SECRET"])


@app.route("/")
def index():
    return "You call index()"


@app.route("/callback", methods=["POST"])
def callback():
    """Messaging APIからの呼び出し関数"""
    # LINEがリクエストの改ざんを防ぐために付与する署名を取得
    signature = request.headers["X-Line-Signature"]
    # リクエストの内容をテキストで取得
    body = request.get_data(as_text=True)
    # ログに出力
    app.logger.info("Request body: " + body)

    try:
        # signature と body を比較することで、リクエストがLINEから送信されたものであることを検証
        handler.handle(body, signature)
    except InvalidSignatureError:
        # クライアントからのリクエストに誤りがあったことを示すエラーを返す
        abort(400)

    return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))
    if user_text == "ブルゾン":
        reply_text = "ちえみ"
    # elif user_text == "外出":
    #     reply_text = "外出中ですね。気をつけて行ってらっしゃい！🚶‍♂️"
    # elif "掃除" in user_text:
    #     reply_text = "掃除状況を記録しました！✨"
    # else:
    #     reply_text = f"「{user_text}」ですね。詳しく教えてもらえると助かります！"

    # 返信を送信


# if __name__ == "__main__":
#     port = int(os.getenv("PORT", 5000))
#     app.run(host="0.0.0.0", port=port)
   line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )
