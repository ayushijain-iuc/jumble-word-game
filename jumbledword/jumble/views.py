from django.shortcuts import render
from django.http import HttpResponse
import random
words=[
    'python',
    'apple',
    'cat',
    'ball',
    'dog',
    'elephant',
    'horse',
    'flutter',
    'butter',
    'what',
    'when',
    'how long',
    ]
def rword():
    global jword
    global word
    word=random.choice(words)
    jum=random.sample(word,len(word))
    jword=''.join(jum)

msg=''
def jumble(request):
    rword()
    global jword,msg
    return render(request,'index.html',{'jumble_word':jword,'msg':msg})

def checkans(request):
    global word,msg,jword
    user_answer=request.GET['answer']
    if user_answer==word:
        msg='that word was a correct one'
        jumble(request)
    else:
        msg='you should try again'
    return render(request,'index.html',{'jumble_word':jword,'msg':msg})
    

# Create your views here.
