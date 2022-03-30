
from django.urls import path
from app_mvt.views import listas_familia


urlpatterns = [
    path('familia/', listas_familia, name = "Familia")
]
