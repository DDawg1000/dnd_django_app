from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('increment/<int:button_id>/', views.increment, name='increment'),
]
