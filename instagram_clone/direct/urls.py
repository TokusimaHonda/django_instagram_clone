from django.urls import path
from direct.views import inbox, Directs, SendDirects, UserSearch, NewConversation

urlpatterns = [
    path('', inbox, name='inbox'),
    path('direct/<username>', Directs, name='directs'),
    path('send/', SendDirects, name='send_directs'),
    path('new/', UserSearch, name='usersearch'),
    path('new/<username>', NewConversation, name='newconversation'),
]
