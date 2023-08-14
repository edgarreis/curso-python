import telebot

bot = telebot.TeleBot('SEU TOKEN AQUI')

@bot.message_handler(commands=['start', 'hello'])
def handle_start(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"seu chat_id: {chat_id}")



# def send_welcome(message):
#    bot.reply_to(message, "Howdy, how are you doing?")


bot.polling()