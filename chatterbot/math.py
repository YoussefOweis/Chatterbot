<<<<<<< HEAD
from chatterbot import ChatBot

bot = ChatBot("Math",logic_adapters=["chatterbot.logic.MathematicalEvaluation"])
print("------------------ Math chatbot ------------------")
while True:
    user_text = input("type the math equation that you want to solve :")
=======
from chatterbot import ChatBot

bot = ChatBot("Math",logic_adapters=["chatterbot.logic.MathematicalEvaluation"])
print("------------------ Math chatbot ------------------")
while True:
    user_text = input("type the math equation that you want to solve :")
>>>>>>> e5ef5242dcdced5f8ed6da685405a024e6d5c53f
    print("chatbot: "+ str(bot.get_response(user_text)))