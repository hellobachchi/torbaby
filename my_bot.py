from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from api import send_mag_link, torrent, list_movies, gen_dow_link
from time import sleep
from config import TOKEN 
import os
user_tasks = []
updater = Updater(TOKEN)


# def purga():
#     while True:
#         sleep(1)
#         if user_tasks:
#             try:
#                 torlist = list_movies()['result']['pageData']
#                 for tit in torlist:
#                     for task in user_tasks:
#                         if tit['torrentDTO']['torrentHash'] in task[2]:
#                             torname = tit['torrentDTO']['torrentName']

#                             if torname != None and tit['torrentDTO']['progress'] == 100.0:
#                                 torhash = tit['torrentDTO']['torrentHash']
#                                 dlink = gen_dow_link(torhash)
#                                 updater.bot.send_message(
#                                     chat_id=task[0], text=torname+"\n\n"+dlink)
#                                 user_tasks.remove(task)
#             except:
#                 pass


def start(update: Update, context: CallbackContext):
    update.message.reply_text(f"Hi {update.message.from_user['first_name']} 👋")
    update.message.reply_text("Send me a torrent or magnet link")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("No Help Bitch!")


def send_mag(update: Update, context: CallbackContext):
    msg = update.message.text
    if 'hi' in msg.lower() or 'hello' in msg.lower():
        update.message.reply_text(
            f"Hello {update.message.from_user['first_name']} 👋 !")
        return
    if 'magnet:?' in msg:
        msg_id = update.message.message_id
        chat_id = update.message.from_user['id']
        user_tasks.append([chat_id, msg_id, msg])
        send_mag_link(msg) 
        update.message.reply_text("Success! We will inform you when the file is ready")

    else:
        update.message.reply_text("NOPE Buddy! I need a magnet link!")


def testing(update: Update, context: CallbackContext):
    updater.bot.send_message(
        chat_id=update.message.from_user['id'], text=f'{update.message.from_user}')


def downloader(update, context):
    myfile = context.bot.get_file(update.message.document)
    reply = torrent(myfile)
    msg_id = update.message.message_id
    chat_id = update.message.from_user['id']
    user_tasks.append([chat_id, msg_id, reply]) 
    update.message.reply_text(
        "Success! We will inform you when the file is ready")



# updater.dispatcher.run_async(purga)
updater.dispatcher.add_handler(MessageHandler(Filters.document, downloader))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('test', testing))
updater.dispatcher.add_handler(MessageHandler(Filters.text, send_mag)) 

updater.start_webhook(listen='0.0.0.0', port=os.environ.get('PORT', 5000), url_path=TOKEN,
                      webhook_url='https://torbaby.herokuapp.com/' + TOKEN)
# updater.start_polling()
updater.idle()
