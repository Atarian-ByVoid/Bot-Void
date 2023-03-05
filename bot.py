import telebot 
import requests

KEY_API="5960212647:AAGTUduWXvTlTQ8STfkW9nzmvFLM9veGYy8"
bot = telebot.TeleBot(KEY_API)


@bot.message_handler(commands=["test1"])
def test1(message): 
      pass
@bot.message_handler(commands=["test2"])
def test2(message): 
      pass
@bot.message_handler(commands=["test3"])
def test3(message): 
      pass
            
@bot.message_handler(commands=["opcao1"])
def option1(message): 
      text = """  
      Escolha um caminho do vazio para seguir
      /test1 Teste1
      /test2 Teste2
      /test3 Teste3"""
      bot.message(message.chat.id, text)



@bot.message_handler(commands=["opcao2"])
def option2(message): 
      pass

@bot.message_handler(commands=["opcao3"])
def option3(message): 
      print(message)
      bot.send_message(message.chat.id,"The Division Of The Void")
      
@bot.message_handler(commands=["opcao4"])
def option4(message): 
      bot.send_photo(message=message, photo=open('images\Sunny.jpg', 'rb'))



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
        /opcao4 teste 4

        Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""

    bot.reply_to(message,text)

#Entra em looping
bot.polling()
