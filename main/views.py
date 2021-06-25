from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import deck, flashCard
from .forms import CreateNewDeck, CreateflashCard

def createFlash(response, id):
    form = CreateflashCard()
    s_deck = get_object_or_404(deck, id=id)
    if not response.user.is_authenticated:
        return HttpResponseRedirect("/")
    if response.method == "POST":
        form = CreateflashCard(response.POST)
        if form.is_valid():
            card = flashCard(
                    deck = s_deck,
                    name = form.cleaned_data["name"],
                    question = form.cleaned_data["question"],
                    answer = form.cleaned_data["answer"]
                )
            card.save() 
        form = CreateflashCard()
    context = {"id":id,"name":s_deck.name, "form":form}
    return render(response, "main/flashcreate.html", context)





def home(response):
    if response.method == "POST":
        form = CreateNewDeck(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = deck(name=n)
            t.save()
            response.user.deck.add(t)
        return HttpResponseRedirect("/")
    
    else:
        form = CreateNewDeck()
    return render(response, "main/home.html", {"form": form })

def question(response, id):
    try:
        card = flashCard.objects.get(id=id)
    except flashCard.DoesNotExist:
            card = None
    if not response.user.is_authenticated:
        pass

    elif card.deck in response.user.deck.all():
        return render(response, "main/question.html", {"card":card, "id":id})
    return render(response, "main/home.html", {})


def answer(response, id):
    try:
        card = flashCard.objects.get(id=id)
    except flashCard.DoesNotExist:
            card = None
    if not response.user.is_authenticated:
        pass

    elif card.deck in response.user.deck.all():
        deck = card.deck
        nextcard = flashCard.objects.filter(deck = deck, id__gt=id).first()
        if nextcard:
            nextlink = "/question-" + str(nextcard.id)
            last = False
        else:
            nextlink = "/"
            last = True

        return render(response, "main/answer.html", {"card":card, "id":id, "nextlink": nextlink, "last": last })
    return render(response, "main/home.html", {})
