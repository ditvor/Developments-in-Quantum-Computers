import logging
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters
from final_project import top_quantum_comp

bot_token = ""
TOKEN = bot_token


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


logger = logging.getLogger()
logger.setLevel(logging.INFO)


updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):  # /start
    logger.info(f'Get /start command from {update.effective_chat.id}')
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Привет, {update.effective_chat.first_name}! Ты написал мне /start")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def qubits(update, context):  # /qubits
    logger.info(f'Get /qubits command from {update.effective_chat.id}')
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Лидером отрасли являтеся компания {top_quantum_comp[0]} "
        f"с их квантовым компьюетром {top_quantum_comp[1]}."
        f" Максимальное количество связанных кубитов: {top_quantum_comp[2]}.")


qubits_handler = CommandHandler('qubits', qubits)
dispatcher.add_handler(qubits_handler)

updater.start_polling()
