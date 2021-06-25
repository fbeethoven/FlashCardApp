from django.urls import path
from . import views

urlpatterns = [
        path("createflash-<int:id>", views.createFlash, name = "createFlash" ),
        path("", views.home, name = "home" ),
        path("home/", views.home, name = "home" ),
        path("question-<int:id>", views.question, name = "question" ),
        path("answer-<int:id>", views.answer, name = "answer" ),
    ]
