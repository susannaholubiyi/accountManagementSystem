from django.urls import path

from demo import views

urlpatterns = [
    path("hello", views.say_hello),
    path("welcome/<str:name>/", views.welcome)
]
