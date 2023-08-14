import telebot

bot = telebot.TeleBot('6532101800:AAHELILoZTFu-Sq-nC1fdoK16q1y13X0rVU')

@bot.message_handler(commands=['start', 'hello'])
def handle_start(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"seu chat_id: {chat_id}")



# def send_welcome(message):
#    bot.reply_to(message, "Howdy, how are you doing?")


bot.polling()