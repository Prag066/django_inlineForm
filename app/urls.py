
from django.urls import path
from .views import *


urlpatterns = [
    # path('',Index),
    path('<int:author_id>/',inlineModelFromView),
]
