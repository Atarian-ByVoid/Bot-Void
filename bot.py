import telebot 

KEY_API="5960212647:AAGTUduWXvTlTQ8STfkW9nzmvFLM9veGYy8"
bot = telebot.TeleBot(KEY_API)


@bot.message_handler(commands=["division1"])
def division1(message): 
      bot.send_message(message.chat.id, "The Division Of The Dark")
@bot.message_handler(commands=["division2"])
def division2(message): 
      bot.send_message(message.chat.id, "The Division Of The Light")
@bot.message_handler(commands=["division3"])
def division3(message): 
      bot.send_message(message.chat.id, "The Division Of The Unknown")

            
@bot.message_handler(commands=["option1"])
def option1(message): 
      text = """  
      Escolha um caminho do vazio para seguir
      /division1 Division Path 1
      /division2 Division Path 2
      /division3 Division Path 3 """
      bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["option2"])
def option2(message): 
      bot.send_message(message.chat.id,"New Wave")

@bot.message_handler(commands=["option3"])
def option3(message): 
      print(message)
      bot.send_message(message.chat.id,"The Division Of The Void")
      

#Vai sempre retornar a mesma messnagem independente da pergunta 
def verify(message):
        return True
 
#Função do bot: Menssagem de boas vindas   
@bot.message_handler(func=verify)
def replied(message): 
    text = """
        Hi, welcome to the void
        Escolha uma opção para continuar(clique no item):
        /option1 teste 1
        /option2 teste 2
        /option3 teste 3
        Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""

    bot.reply_to(message,text)

#Entra em looping
bot.polling()
