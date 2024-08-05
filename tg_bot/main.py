from telegram.ext import Updater
from tg_bot.modules import register_modules
from tg_bot.utils.logging import setup_logging

def main():
    setup_logging()
    updater = Updater("YOUR_TOKEN", use_context=True)
    dispatcher = updater.dispatcher

    register_modules(dispatcher)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
