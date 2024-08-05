from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

def other_command(update: Update, context: CallbackContext):
    update.message.reply_text('This is another command!')

def register(dispatcher):
    dispatcher.add_handler(CommandHandler('other', other_command))
