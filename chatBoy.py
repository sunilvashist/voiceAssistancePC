import os
from chatterbot import ChatBot
from chatterbot.trainers import  ListTrainer

#make sure to insttall chatterbot-corpus

def runChatBot(voice):
    bot=ChatBot('Jarvis')
    trainer=ListTrainer(bot)

    dataDir="C:\\Vaibhaw\\Development\\Jarvis\\chatterbot-corpus-master\\chatterbot_corpus\\data\\english\\"
    for files in os.listdir(dataDir):
        data=open(dataDir+files,'r').readlines()
        trainer.train(data)
    return bot.get_response(voice)


