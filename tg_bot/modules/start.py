from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! I am your bot.\n How would you like me yo serve you today?')

def register(dispatcher):
    dispatcher.add_handler(CommandHandler('start', start))
