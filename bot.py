from pyrogram import Client,Filters
from googletrans import Translator
import time
app = Client(
    "mytgbot",
    api_id= "api id here",
    api_hash="api hash here",
    bot_token="bot token here"
)

@app.on_message(Filters.command(["start"]))
def start(client, message):
    client.send_message(
        chat_id=message.chat.id,
        text="Hi {}".format(message.from_user.first_name))
    time.sleep(1)
    client.send_message(
           chat_id=message.chat.id,
           text="Enter the text to convert")

@app.on_message(Filters.text)
def echo(client, message):
    msg=message.text
    translator=Translator()
    ts=translator.translate(msg,dest='ml')
    new=client.send_message(chat_id=message.chat.id,text="Translating...")
    time.sleep(2)
    new.edit(ts.text)
app.run() 
