from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from bot import views, bot

urlpatterns = [
    path('bot/', csrf_exempt(bot.webhook)),
    path('admin/', admin.site.urls),
]
