from django.urls import path
from . import views

urlpatterns = [
    path('', views.ChatListView.as_view(), name='chat_list'),
    path('<int:id>/', views.ChatView.as_view(), name='chat'),
    path('create', views.CreateChatView.as_view(), name='create_chat')
]
