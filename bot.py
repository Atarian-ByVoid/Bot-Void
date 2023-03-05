import telebot 


KEY_API="5960212647:AAGTUduWXvTlTQ8STfkW9nzmvFLM9veGYy8"
bot = telebot.TeleBot(KEY_API)




@bot.message_handler(commands=["opcao1"])
def option1(message): 
      pass

@bot.message_handler(commands=["opcao2"])
def option2(message): 
      pass

@bot.message_handler(commands=["opcao3"])
def option3(message): 
      bot.send_photo()










#Vai sempre retornar a mesma messnagem independente da pergunta 
def verify(message):
        return True
 
#Função do bot: Menssagem de boas vindas   
@bot.message_handler(func=verify)
def replied(message): 
    text = """
        Hi, welcome to the void
        Escolha uma opção para continuar(clique no item):
        /opcao1 teste 1
        /opcao2 teste 2
        /opcao3 teste 3
        Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""





    bot.reply_to(message,text)







#Entra em looping
bot.polling()
