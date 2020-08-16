#import re
#from flask import Flask, request
#import telegram
#from telegram.passport.credentials import bot_token, bot_user_name,URL

#imports
import os
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from wit import Wit

"""bot credentials"""
TOKEN = "1174443046:AAH39jAknodjzwQkXVtsQtME0j0tY2ZuIx8"
PORT = int(os.environ.get('PORT','8443'))
BOT_USER_NAME = "Talkbuddy_bot"
URL = "https://talkbuddybot.herokuapp.com/"

"""ai token"""
AI_TOKEN = "BDAETOIRN7UQDCSTRKFAQXBMR45I3JY3"
   
#Enable Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

#Define few commands handlers
def start(update, context):
   """When /start is hit"""
   update.message.reply_text('Hi!')

def help_command(update, context):
   """When /help is hit"""
   update.message.reply_text('Help!')

def echo(update, context):
   """Echo the user message."""
   #setting wit ai
   ai = Wit(access_token = AI_TOKEN)
   resp = ai.message(update.message.text)

   print(str(resp))
   update.message.reply_text(str(resp))
   
def main():
   """start the bot"""
   updater = Updater(TOKEN, use_context=True)

   #get the dispatcher to register handlers
   dp = updater.dispatcher

   #on different commands answer in telegram
   dp.add_handler(CommandHandler("start",start))
   dp.add_handler(CommandHandler("help",help_command))

   #to reply the same text back
   dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
   
   #start the bot
   updater.start_polling()
   #updater.start_webhook(listen = "0.0.0.0",
   #                      port = int(PORT),
   #                      url_path = TOKEN)
   #updater.bot.set_webhook(URL+TOKEN)
   updater.idle()

if __name__ == '__main__':
   main()
