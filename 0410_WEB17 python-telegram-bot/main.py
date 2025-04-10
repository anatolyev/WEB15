import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from telegram import ReplyKeyboardMarkup
from config import BOT_TOKEN

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

async def keyboard1(update, context):
    reply_keyboard = [['/start', '/help'],
                      ['/set 5', '/set 10', '/set 30', '/set 60', '/unset']]
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

# Добавлены задачи
async def alarm(context) -> None:
    """Send the alarm message."""
    job = context.job
    await context.bot.send_message(job.chat_id, text=f"Beep! {job.data} seconds are over!")


def remove_job_if_exists(name, context) -> bool:
    """Remove job with given name. Returns whether job was removed."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


async def set_timer(update, context) -> None:
    """Add a job to the queue."""
    chat_id = update.effective_message.chat_id
    try:
        # args[0] should contain the time for the timer in seconds
        due = float(context.args[0])
        if due < 0:
            await update.effective_message.reply_text("Простите мы не можем вернуться в прошлое!")
            return

        job_removed = remove_job_if_exists(str(chat_id), context)
        context.job_queue.run_once(alarm, due, chat_id=chat_id, name=str(chat_id), data=due)

        text = "Таймер установлен!"
        if job_removed:
            text += " Предыдушей таймер удален."
        await update.effective_message.reply_text(text)

    except (IndexError, ValueError):
        await update.effective_message.reply_text("Используйте: /set <секунд>")


async def unset(update, context) -> None:
    """Remove the job if the user changed their mind."""
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = "Таймер удален!" if job_removed else "Нет активных таймеров."
    await update.message.reply_text(text)




def main():
    application = Application.builder().token(BOT_TOKEN).build()
    # Регистрация команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(CommandHandler("set", set_timer, has_args=True))
    application.add_handler(CommandHandler("unset", unset))


    # Обработка и запуск (в конце)
    text_handler = MessageHandler(filters.TEXT, echo)
    application.add_handler(text_handler)
    application.run_polling()

if __name__ == '__main__':
    main()

