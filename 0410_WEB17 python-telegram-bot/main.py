import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from config import BOT_TOKEN

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

async def keyboard1(update, context):
    reply_keyboard = [['/start', '/help']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    return markup



async def echo(update, context):
    await update.message.reply_text(update.message.text)


async def start(update, context):
    user = update.effective_user
    markup = await keyboard1(update, context)

    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Я эхо-бот."
        rf"Напишите мне что-нибудь, и я пришлю это назад!",
        reply_markup=markup
    )


async def help_command(update, context):
    user = update.effective_user
    await update.message.reply_text("Я пока ничего не умею и даже не умею помогать... "
                                    "я только ваше эхо.")



def main():
    application = Application.builder().token(BOT_TOKEN).build()
    # Регистрация команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))



    # Обработка и запуск (в конце)
    text_handler = MessageHandler(filters.TEXT, echo)
    application.add_handler(text_handler)
    application.run_polling()

if __name__ == '__main__':
    main()

