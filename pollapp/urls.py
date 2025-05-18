from django.urls import path

from pollapp.views import create_poll, index, poll_detail, addvote

urlpatterns = [
    path('', index, name='home'),
    path('poll/<int:poll_id>', poll_detail, name='poll_detail'),
    path('addvote/<int:variant_id>', addvote, name='addvote'),
    path('createpoll/', create_poll, name='create_poll')
]
