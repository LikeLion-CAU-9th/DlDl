
from django.urls import path
from .views import *

urlpatterns = [
    path('', designer_home, name = "designer_home"),
    path('<str:id>', detail, name = "detail"),
    path('new/', new, name = "new"),
    path('create/', create, name = "create"),
    path('portfolio_upload/', portfolio_upload, name = "portfolio_upload"),
    
    
    
    
]