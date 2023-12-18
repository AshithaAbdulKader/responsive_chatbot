from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('chatbot', read_only=False, 
              logic_adapters=[
                 {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response':'sorry, i dont know what that means ',
                    'maximum_similiarity_threshold': 0.90
                     }
                     
                     ])

List_to_train = [
   "hi",
   "hi,whatsapp",
   "whats your name",
   "iam your listener"
]

List_trainer = ListTrainer(bot)
List_trainer.train[List_to_train]

def index(request):
    return render(request,'blog/index.html')

def specific(request):
    return HttpResponse("list")

def getResponse(request):
  userMessage =  request.GET.get('userMessage')
  chatResponse = str(bot.get_response(userMessage))
  return HttpResponse(chatResponse)


