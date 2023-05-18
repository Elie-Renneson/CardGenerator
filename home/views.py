from django.shortcuts import render, redirect
from .models import Phrase


def home(request):
    phrases = Phrase.objects.all()
    return render(request, 'home.html', {'phrases': phrases})

def ajouter_phrases(request):
    if request.method == 'POST':
        phrases_texte = request.POST['phrases']
        phrases_liste = phrases_texte.split(';')
        for phrase in phrases_liste:
            if phrase.strip() != '':
                Phrase.objects.create(texte=phrase.strip())
    return redirect('home')
