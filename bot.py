import telebot 


CHAVE_API="5960212647:AAGTUduWXvTlTQ8STfkW9nzmvFLM9veGYy8"

bot = telebot.TeleBot(CHAVE_API)



@bot.message_handler()
def responder(menssagem):
    bot.reply_to(menssagem,"Hi, Welcome to the void")


bot.polling()
