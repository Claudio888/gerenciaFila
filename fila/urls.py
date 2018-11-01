from django.contrib import admin
from django.urls import path, include
from .views import AddFila
from .views import ChamarFila
from .views import Home
from .views import mylogout
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('add/', AddFila, name='adicionarfila'),
    path('chamar/', ChamarFila , name='chamarfila'),
    #path('getAction', ChamarFila),
    path('',Home, name='home'),
    path('logout/', mylogout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)